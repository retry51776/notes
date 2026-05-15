# ComfyUI

## Table of Contents

- [Paths](#paths)
- [Common Failure Modes](#common-failure-modes)
- [Recovery Moves](#recovery-moves)

## Paths

default workflow path: ~/Documents/ComfyUI/user/default/workflows

## Common Failure Modes

- Check Hardware support precision BEFORE download model
- FP8 formats (E4M3, E5M2) is NOT support by mac os
- VAE failed on mps backend, launch ComfyUI with `--cpu-vae` flag
- ACE 1.5 can't generate song above 500 seconds.
- Ksampler ALWAYS set to `sample_name=euler_ancestral, scheduler=beta`

## Recovery Moves

### Check Hardware support precision BEFORE download model

Mac usually only support fp16, but common default model are fp8.
