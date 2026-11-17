# Voxel Fauna · Design System

The look in one page. The numbers live in `_system/studio/blender/vf_standards.py` (and, generated from it, in the
skill's standards table); this page says what they are for. Approved sheets are in `Reference/`.

## Identity
A collection of animal portraits that belong together: every animal seen from the same true-isometric camera, built
in the same **bulky blocky-mob** style (a few big sharp-edged sections per animal, turned a little at their joints in
a pose that fits its personality, an expressive face drawn on the front of the head), lit by the same rig, matte, in
vivid flat solid colours, each on its own soft, muted flat colour. Bigger animals are built from more, finer voxels.
Recognition comes from proportions, pose and three to five species features carried by large blocks, never from
detail. The information artworks speak in a friendly, Duolingo-like voice with chunky cards.

## The picture
| Element | Rule |
|---|---|
| Camera | orthographic, azimuth 45°, elevation 35.264° (true isometric), deep focus |
| Facing | head lower right; the face and the left flank visible together |
| Voxel | 0.1 m; the posed longest side scales with the real size: 28 × L^0.4 ± 15 % voxels (fox 29, lion 42, giraffe 53; approved 2026-11-16, was 16–32 for all) |
| Geometry | `mob`: one box per part (body, big head, pillar legs, slab ears, block tail; a second box only for a real feature), flat planes, sharp edges, no bevel; no rounded or stair-stepped curves (approved 2026-11-16, owner: "minecraft mobs vibes"; was `merged`, bevelled, approved 2026-11-15) |
| Pose | sections turn at their joints (≤ 40°), ears and brows follow the head; one pose per species from its personality (sly fox mid-sneak, flamingo on one leg, sleepy koala) |
| Stacking | each section is its own layer: overlapping sections both stay whole, so a turned section never leaves a hole (owner: "stack the block, dont make a hole of it") |
| Plates | switched off for now (owner, 2026-11-16: "disable flat pixel for now"): every part, feet included, is whole voxels |
| Face | an expression painted flat on the front of the head (owner: "they should flat", block-game character reference): a white eye with the pupil to the inside (or a dark eye with a glint, or a sleepy line), a darker brow strip whose steps carry the mood, a painted mouth; a snout box with a dark nose row on its top front edge |
| Material | matte (roughness 0.86, specular 0.3, no coat, no subsurface); flat solid colours, no texture, no shading painted in colour (owner: "keep the texture flat solid") |
| Style source | the blocky-mob style of block-building games, never a copy of a particular game's creature and never named after a game anywhere (titles, keywords, listings) |
| Colour | Khronos PBR Neutral view, neutral slate-100 sky fill: colours render as authored (owner 2026-11-16: "the model colour is so pale" under AgX). PROPOSED v2.3 (owner 2026-11-17: "edit all the animal model color to not that vibrant", with a reference sheet): every animal colour is calmed at render time by `vf_standards.ANIMAL_TONE` (OKLCH lightness and hue kept, chroma above 0.09 halved, then x 0.95: orange-600 0.217 -> 0.146), so palettes in `animal.json` keep their tokens |
| Palette | Tailwind v4 tokens by default, a hex where none fits (owner 2026-11-16: "break from tailwind coloring token"); 3–7 keys; large areas shades 50–800, details any shade |
| Background | one colour per species (Tailwind 50–300 or a soft hex), complementary, rendered as a **vivid pastel** (OKLCH chroma ≤ 0.07, lightness 0.85–0.93, hue kept; owner: "vivid but pastel (not too vibrant or neon), keep it calm"), ΔE ≥ 30 between the main colour and the rendered background; exactly that hex in every open pixel; card lips and the fun-fact card get the same chroma factor |
| Light | warm key sun front-left and 55° high (`iso_top`, approved 2026-11-15), cool rim behind without its own shadow |
| Shadow | one soft shadow on the ground, strength 0.65, composited over the background |
| Framing | the whole animal, centred; illustrations fill 70 % (1:1), 82 % (9:16 width), 68 % (16:9 height) on the binding side |
| Brand | none in the images |

## Choosing a background
1. Name the animal's main coat colour family (orange fox, grey koala, black-and-white panda).
2. Start from the opposite family (orange ↔ teal/cyan/sky, yellow-amber ↔ violet/indigo, pink ↔ emerald, red ↔ teal);
   for neutral animals pick a soft colour of their world (bamboo lime for the panda, Arctic blue for the polar bear,
   sunny amber for the grey koala).
3. Shade 200 (300 for very light animals, or when the muted 200 sits too close to white fur, as for the panda);
   `vf.py check` enforces ΔE ≥ 30 against the muted colour; the preview must separate the animal at thumbnail size.
4. Write the reason in `animal.json → look.why`. Animals may share a background.

The first twenty-five (all rendered as calm pastels): fox teal-200, panda #BFD7A7 (the pastel of lime-400: the lime and
green pastels sit too close to its white fur), red panda cyan-200, penguin sky-200, capybara indigo-200, flamingo
emerald-200, koala amber-200, lion violet-200, polar bear blue-300, giraffe sky-300, elephant orange-200, tiger green-200, toucan
blue-200, hippo yellow-200, hedgehog emerald-100, axolotl cyan-200, wolf indigo-200, green sea turtle sky-200,
armadillo lime-200, macaw emerald-200, dolphin orange-100, mountain goat violet-300 and zebra orange-300 (white coats
need a stronger shade to stay ΔE 30 away), rabbit lime-200, tree frog pink-200.

## The information artwork (Duolingo-style cards)
| Element | Rule |
|---|---|
| Arrangements | 1:1 header and photo across the top, stat tiles beside the animal, three cards in a bottom band · 9:16 header, the animal with the photo beside it, 2×2 stats, three stacked cards · 16:9 the animal left; header + photo, 2×2 stats, three cards side by side on the right |
| Cards | white, rounded (2.2u), a darker lip under each (0.9u, background + 200), 2.0u padding (1.3u in stat tiles), 2.2u gutters, the text centred in its card; flat, no gradients or shadows (approved 2026-11-16, owner: "make it breathe") |
| Icons | 8 × 8 pixel-art icons in a rounded badge (the background family one step lighter, the icon at 600): house, apple and light bulb on the card headings; span, weight, heart, egg, bolt or star on the stat tiles by their label |
| Fun fact | a full-colour card in the background's family at 700 with white type |
| Photo | a real photograph in a thick white frame (1.0u) with a lip, pasted like a sticker tilted −3°, cropped to fill; credit underneath: `Photo: <author> · <licence>` |
| Status | the IUCN chip in the status colour (LC emerald, NT lime, VU amber, EN orange, CR red) |
| Type | Poppins: kicker Bold caps in a dark pill · name ExtraBold (≤ 2 lines) · scientific name italic · labels Bold tracked caps · values ExtraBold · body Medium · fun fact SemiBold |
| Unit | u = 1 % of the short side |
| Copy | `kicker` (Class · family in plain English), 4 stats (label ≤ 12, value ≤ 11), Home turf ≤ 100, On the menu ≤ 95, one fun fact ≤ 115 characters |
| Voice | short, warm, concrete, a surprising bit first, everyday comparisons, at most one exclamation per card; no AI-slop words (majestic, fascinating, crucial role, truly, delve); hypotheses said as such |
| Fit | type never shrinks; too much text is an error naming the field; numbers stay with their unit when lines wrap |

## The A5 card (APPROVED and locked 2026-11-17, standards v2.2 + the export package; owner: "the animal and info size should be built in card in a5 size in pdf")

| Element | Rule |
|---|---|
| Size | A5 portrait, 148 × 210 mm, 3 mm bleed on every side, 300 dpi; PDF pages with the trim box set; one card per language (`CARD-EN`, `CARD-ID`) |
| Units | u = 1 % of the trim width (1.48 mm); a 6u margin keeps everything clear of the trim |
| Front | v3, minimal and playful, no photograph, laid out by principle (owner, 2026-11-17: "push the limit of design. use best practice of design to judge them"): hierarchy name, model, numbers, words, fun fact; one left edge at an 8u margin; a 2u spacing rhythm; one type scale (ratio 1.25 from 1.6u = 6.7 pt: 1.6, 2.0, 2.5, 3.1, title 9.5); groups separated by space, not lines; nothing readable within 4.2u (6.2 mm) of the trim; contrast checked in code (4.5:1 body, 3:1 large). Top line: the kicker left (no collection number), the Nilant wordmark right ("nilant" alone, no head; 2.2u tall, the dark-type version on a light background, the white on a dark one; owner 2026-11-17: "add nilant logo ... on top right", then "remove the nilant icon so it show the nilant text only"). The name, the scientific name with the IUCN chip. The hero (v4, owner 2026-11-17: "remove the circle, scatter more particles ... keep the model shadow"): no circle; the model, its body centred horizontally on the card (the shadow trails off to the side; owner 2026-11-17), with its own rendered shadow, taken from the dynamic master (shadow = master / background, multiplied onto the card, so it falls on the particles too); 12 small particles around it, never on the animal, in the background family's 400/500/600 tints (no near-white ones; owner 2026-11-17: "make the particle less occur, remove white particle") and five shapes (square, dot, ring, triangle, plus), seeded by the code so a card always comes out the same. Two by two stats (pixel icon badge, label over value). Home and menu in two columns on the same edges. The base: the fun fact on a full-bleed band in the family's 700 with a straight top edge (v4) |
| Back | the regular blocky master cropped to the card on the animal's background; "powered by" + the ihdyo mark + "ihdyo" centred at the bottom, small, in black on a light background and white on a dark one (owner, 2026-11-17); the only brand anywhere |
| Indonesian | the same layout; headings "Rumahnya", "Menu makan", "Fakta seru!", IUCN names in Indonesian (Risiko Rendah, Hampir Terancam, Rentan, Genting, Kritis …), the copy from `animal.json → i18n.id` |
| Type | the card system's fonts and colours; sizes in u: title 7.2, scientific 3.0, kicker 1.9, stat value 3.0, body 2.15, fun fact 2.2, credit 1.15; type never shrinks (too long = an error naming the field) |

## Files
`Color/tailwind-v4-palette.json` (copy of Nilant's), `Fonts/` (Poppins, OFL), `Reference/` (approved look sheets:
rig and geometry 2026-11-15, colour fidelity 2026-11-16, blocky mob before-after, bulky posed before-after and flat faces before-after 2026-11-16; the last is the approved
look, standards v2.0).
