
# Visual

<https://huggingface.co/spaces/ArtificialAnalysis/Text-to-Image-Leaderboard>

<https://huggingface.co/spaces/ArtificialAnalysis/Video-Generation-Arena-Leaderboard>

## Metric

- space persistent
- photorealist
- Action Prediction

## ComfyUI

Prompt
  ↓
CLIP Encoder
  ↓
Text Embedding
  ↓
Diffusion Model attention conditioning

- CFG (Classifier-Free Guidance) `prompt weight`

```md
Huggingface Modals default is BF8 for nvidia hardware, so find Modal is fp16 format able to run in mac.

The problem is from MLX does NOT support fp8, so pytorch can't run fp8 on mac.
Here is github issue link: https://github.com/ml-explore/mlx/issues/1670

```

## LTX

- Storyboard Builder
  - start & end frame
- character reference sheet `picture & prompt for ground consistent across videos`
- camera control formula
  - Snap zoon
  - rack focuses
  - Pan Left/Right
  - Tile Up/Down

- Multi‑model LLMs(MLLM): Gemini 2.0 Flash, LLaMA‑3.2‑11B‑Vision‑Instruct, Pixtral 12B, DeepSeek VL.
  - vision
    - patch16 → 16×16 pixel ~ 768 values possible combination; Common uses Vision path size
  - text
  - audio
    - Spectrogram Patches
      - 2D patches → 16×16 time/frequency
    - Codebook `pre-defined, finite "vocabulary" of sounds; Under millions, common around thousands;`
      - 2 to 8 frames bundle
  - touch?
- OCR tools: Tesseract, EasyOCR.  
- Document processing: Amazon Textract, Google Document AI, pymupdf4llm, marker.

### LatentSync

Generate video sync with audio.

## Dino V3

- Gram Anchoring

### Audio

- Whisper (OpenAI) – speech‑to‑text.
