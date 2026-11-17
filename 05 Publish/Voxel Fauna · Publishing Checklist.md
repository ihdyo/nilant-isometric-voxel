# Voxel Fauna · Publishing Checklist

## Before any upload (per animal)
- [ ] The owner approved the animal (`animal.json → approvals.final`).
- [ ] `vf.py verify` passes; `vf.py check <code> --strict` has no errors.
- [ ] The export package in `export/`: two 4096 masters, the loop GIF, the English and Indonesian
      cards; each looked at full size (no artefacts, type correct, the cards at 100 %).
- [ ] No logo, watermark, signature or URL in the masters, the stock image or the loop (the card back carries
      "powered by ihdyo" only).
- [ ] `vf.py stock <code>` ran: `export/VF-<code>-STOCK.jpg` is 4–100 MP and ≤ 45 MB; CSVs in `05 Publish/Stock/`.
- [ ] Titles and keywords read well (`animal.json → stock` to override the defaults); the species and scientific
      name are in the title; no other brand or trademark.

## Adobe Stock
- [ ] The stock image only: the cards carry a third-party photo (see the Stock Platforms guide).
- [ ] Upload `VF-<code>-STOCK.jpg`.
- [ ] Upload `<code> · Adobe Stock.csv` in the portal; check category Animals.
- [ ] "Created using generative AI tools" stays **unticked** (Blender model and render; no generative image tool).
- [ ] Submit; set the registry's Adobe Stock cells to Submitted.

## Shutterstock
- [ ] Upload the JPEGs, apply `<code> · Shutterstock.csv`, mark as illustration; submit; registry → Submitted.

## Gumroad
- [ ] The zip from `05 Publish/Gumroad/`, the cover image (brand allowed there), the listing text and the licence.
- [ ] Publish; registry Gumroad cells → Live.

## Log every event (as Nilant logs each upload)
- [ ] After each upload: `vf.py log <code> "<platform>" Submitted [--kinds ILL]` (all images of the animal) or
      `vf.py log <Image ID> "<platform>" Submitted`.
- [ ] After review: `vf.py log <Image ID> "<platform>" Accepted --link <url>` (or Rejected `--note "<reason>"`, Live).
      It writes the dated row to the registry's Publish Log sheet and `05 Publish/Voxel Fauna · Publish Log.md`, and
      sets the image's platform cell. Refusal reasons shape the next uploads: note them.
