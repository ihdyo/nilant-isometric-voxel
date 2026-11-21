# Colour

Every colour in Voxel Fauna is a hex code `#RRGGBB` (owner, 2026-11-21: "remove the tailwind color palette
completely"). The Tailwind v4 palette that used to live here was removed; every token the project used was replaced
by its exact hex value, so nothing renders differently.

- **Animal palettes** (`animal.json → look.palette`): 3–7 keys per species, hex. They render calmed
  (`vf_standards.ANIMAL_TONE`).
- **Backgrounds** (`look.background`, with `background_oklch` and `background_name`): one OKLCH chroma for the whole
  collection (0.06) at lightness 0.87, the hue chosen per animal from its habitat or as the complement of its coat
  (`vf_standards.BACKGROUND_RULE`, `vf_color.background(hue, L, C)`). Lightness moves (0.74–0.88) only where the
  coat would not stand out.
- **Card colours** come from the background's hue on the collection's own ramp, `vf_color.RAMP` (shades 50–950 of
  OKLCH lightness and a calm chroma), written `#RRGGBB-700` in code (the background's hue at shade 700).
- **Light rig, sky fill and IUCN chips:** hex constants in `vf_standards.py`.
