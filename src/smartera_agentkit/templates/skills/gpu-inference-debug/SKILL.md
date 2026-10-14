---
name: gpu-inference-debug
description: Diagnose GPU inference failures using model, runtime and driver evidence.
---

# gpu-inference-debug

1. Capture model size/format, runtime version, device and VRAM availability.
2. Verify driver/CUDA/PyTorch or inference-server compatibility with actual commands.
3. Separate OOM, device selection, unsupported kernel and broken model.
4. Recommend isolated reversible tests before configuration changes.
5. Never install drivers, download weights or switch CPU policy without authorization.

Inputs: task context and verified project state.

Output: evidence-backed findings and proposed changes.

Verification: report executed checks and checks not run.
