# Online IDE

```bash
# Save docker image in volume, not on default system folder
docker save myimage:latest -o /workspace/cache/myimage.tar
# later
docker load -i /workspace/cache/myimage.tar

docker pull nvcr.io/nim/nvidia/llama3.1-nemotron-nano-4b-v1.1:latest
docker save nvcr.io/nim/nvidia/llama3.1-nemotron-nano-4b-v1.1:latest -o llama3.1-nemotron-nano-4b-v1.1.tar 

docker load -i llama3.1-nemotron-nano-4b-v1.1.tar
```
