#!/usr/bin/env python3
import struct
import sys
from collections import Counter
from pathlib import Path

GGML_TYPES = {
    0: "F32", 1: "F16", 2: "Q4_0", 3: "Q4_1",
    6: "Q5_0", 7: "Q5_1", 8: "Q8_0", 9: "Q8_1",
    10: "Q2_K", 11: "Q3_K", 12: "Q4_K", 13: "Q5_K",
    14: "Q6_K", 15: "Q8_K", 16: "IQ2_XXS", 17: "IQ2_XS",
    18: "IQ3_XXS", 19: "IQ1_S", 20: "IQ4_NL", 21: "IQ3_S",
    22: "IQ2_S", 23: "IQ4_XS", 24: "I8", 25: "I16",
    26: "I32", 27: "I64", 28: "F64", 29: "IQ1_M",
    30: "BF16", 31: "Q4_0_4_4", 32: "Q4_0_4_8",
    33: "Q4_0_8_8", 34: "TQ1_0", 35: "TQ2_0",
    36: "IQ4_NL_4_4", 37: "IQ4_NL_4_8", 38: "IQ4_NL_8_8",
    39: "MXFP4", 40: "NVFP4", 41: "Q1_0",
}

SCALAR_FMT = {
    0: "<B", 1: "<b", 2: "<H", 3: "<h",
    4: "<I", 5: "<i", 6: "<f", 7: "<?",
    10: "<Q", 11: "<q", 12: "<d",
}

def read_string(f):
    n, = struct.unpack("<Q", f.read(8))
    return f.read(n).decode("utf-8", "replace")

def read_value(f, value_type):
    if value_type == 8:  # string
        return read_string(f)

    if value_type in SCALAR_FMT:
        fmt = SCALAR_FMT[value_type]
        return struct.unpack(fmt, f.read(struct.calcsize(fmt)))[0]

    if value_type == 9:  # array
        elem_type, = struct.unpack("<I", f.read(4))
        count, = struct.unpack("<Q", f.read(8))
        return [read_value(f, elem_type) for _ in range(count)]

    raise RuntimeError(f"Unhandled GGUF metadata value type: {value_type}")

def inspect_gguf(path):
    counts = Counter()
    examples = {}
    metadata = {}

    with path.open("rb") as f:
        magic = f.read(4)
        if magic != b"GGUF":
            raise RuntimeError(f"{path} is not a GGUF file")

        version, = struct.unpack("<I", f.read(4))
        tensor_count, kv_count = struct.unpack("<QQ", f.read(16))

        for _ in range(kv_count):
            key = read_string(f)
            value_type, = struct.unpack("<I", f.read(4))
            metadata[key] = read_value(f, value_type)

        for _ in range(tensor_count):
            name = read_string(f)

            n_dims, = struct.unpack("<I", f.read(4))
            f.seek(8 * n_dims, 1)  # dimensions

            tensor_type_id, = struct.unpack("<I", f.read(4))
            f.seek(8, 1)  # tensor data offset

            tensor_type = GGML_TYPES.get(tensor_type_id, f"UNKNOWN_{tensor_type_id}")
            counts[tensor_type] += 1
            examples.setdefault(tensor_type, name)

    return {
        "path": path,
        "version": version,
        "tensor_count": tensor_count,
        "kv_count": kv_count,
        "metadata": metadata,
        "counts": counts,
        "examples": examples,
    }

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} /path/to/model.gguf-or-directory", file=sys.stderr)
        sys.exit(2)

    target = Path(sys.argv[1]).expanduser()

    if target.is_dir():
        paths = sorted(target.glob("*.gguf"))
    else:
        paths = [target]

    if not paths:
        print("No .gguf files found", file=sys.stderr)
        sys.exit(1)

    total = Counter()

    for path in paths:
        result = inspect_gguf(path)
        total.update(result["counts"])

        md = result["metadata"]
        print(f"\nFILE {path.name}")
        print(f"version: {result['version']}")
        print(f"tensor_count: {result['tensor_count']}")
        print(f"kv_count: {result['kv_count']}")

        for key in [
            "general.name",
            "general.architecture",
            "general.file_type",
            "general.quantization_version",
            "split.no",
            "split.count",
            "split.tensors.count",
        ]:
            if key in md:
                print(f"{key}: {md[key]}")

        print("tensor type counts:")
        for tensor_type, count in result["counts"].most_common():
            example = result["examples"][tensor_type]
            print(f"  {tensor_type}: {count} example={example}")

    if len(paths) > 1:
        print("\nCOMBINED tensor type counts:")
        for tensor_type, count in total.most_common():
            print(f"  {tensor_type}: {count}")

if __name__ == "__main__":
    main()