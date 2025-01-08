#Work in progress...

## Single Shot Multibox Detector

Potential ideas, in a nutshell:
1. Choosing a Lightweight Baseline: e.g., SSD-lite or YOLO-lite with a small backbone (EfficientNet family, DenseNet, ENAS for selecting ideal architecture).
2. Adding Targeted Improvements:
  - Introducing anchor-free heads will simplify anchor engineering.
  - Incorporating attention or minimal Transformer blocks for better long-range context.
  - Using strong data augmentation (Mosaic, MixUp) for better small-object coverage.
3. Distilling from a Powerful Teacher: Training a bigger model on the same dataset and distilling the knowledge into our chosen architecture.
4. Optimizing Speed & Size: Applying pruning and quantization to get real-time FPS on our hardware.
5. Ablate and Validate: Thoroughly testing each component’s contribution using standard benchmarks (COCO, VOC) and real-world scenarios if possible.

