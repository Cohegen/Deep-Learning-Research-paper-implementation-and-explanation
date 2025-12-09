# assets/

This directory stores images, diagrams, and other visual assets used in the project.

Usage notes

- Purpose: Keep figures, diagrams, and photos that accompany notebooks, reports, and READMEs.
- File types: Prefer PNG, JPEG, SVG (for vector diagrams). Use WEBP for compressed images if supported.
- Naming: Use descriptive, kebab-case names, e.g. `resnet-architecture.svg`, `attention-tiling-illustration.png`.
- Organization: Create subfolders when helpful, e.g. `figures/`, `diagrams/`, `photos/`.
- Sizes: Keep large original images in an `originals/` subfolder and add smaller web-friendly copies for docs.
- Attribution: If an asset is from an external source include a short `CREDITS.md` or a caption with source.

Example structure

```
assets/
  figures/
    resnet-architecture.svg
  diagrams/
    flash-attention-tiling.png
  originals/
    photo-raw-2025-08-01.CR2
  README.md
```

If you'd like, I can also add subfolders (`figures`, `diagrams`, `originals`) now — tell me which ones to create.