
# Visual

<https://huggingface.co/spaces/ArtificialAnalysis/Text-to-Image-Leaderboard>

<https://huggingface.co/spaces/ArtificialAnalysis/Video-Generation-Arena-Leaderboard>

## General
- `ffmpeg` common linux package.

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


## Tesla AI

Self Driving Components:
- Occupancy Network  
- Lane Network  
- Traffic Control  
- Road Sign Network  
- Moving Object Network  
- Path Planning Network  

## Occupancy
>
> Converts raw sensor data into a base geometry layer (i.e., things near the vehicle without identifying them).  
> Produces a 3‑D vector space, determines whether objects are static or moving, and predicts motion of unidentified objects. Runs every 10 ms.

### Tesla Dataflow

1. 8 camera streams → raw data.  
2. RegNets & BiFPNs extract features.  
3. Spatial Attention focuses on selected features (spatial & multi‑camera query embeddings).  
4. Temporal Alignment joins vehicle telemetry to create spatio‑temporal features.  
5. Occupancy & Occupancy Flow generate volumetric output via deconvolution networks (current surroundings + predictions).  
6. Drivable Surface & Queryable Output feed downstream processes.  

*NeRF*: 3‑D reconstruction from occupancy data.

## Lane & Object Detection

- Predict lanes and future object behavior.  
- Lane connectivity uses satellite maps to generate lane graphs; these can produce training data or serve as input for planning.  
- Tesla aggregates global lane maps (world‑scale) by merging trips, performing pairwise matching, surface refinement, and auto‑detecting new routes.  

### Dataflow

1. 8 camera streams → geometry extraction.  
2. Combine with navigation map → Lane Guidance Module.  
3. World tensor → lane graphs & adjacency matrix.

## Path Planning (Decision Layer)
>
> Makes decisions every 50 ms.

- Considers all possible interactions and aligns planning to interaction cost (~10 ms).  
- **Goal Candidates**: most likely solutions.  
- **Seed Trajectories**: predicted trajectories of other agents.  
- **Interaction Search**: combines seed trajectories with goal candidates; scores each interaction and selects the best goal candidate using a neural planner.  

## Auto‑Labeling
>
> Labels lanes, planners, objects, shapes, occupancy, etc., similar to a factory line (yield, quality, quantity, inventory).

## Simulation Inputs

- Lane graph  
- Weather conditions  
- Road participants  
- Scenarios (e.g., trophies)

## Data Management
>
> Identify problematic prediction datasets (“challenge cases”) and find similar examples.  

Vehicle signals are detected by sub‑networks that infer car status.
