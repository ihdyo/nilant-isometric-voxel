# Voxel Fauna · Design System

The look in one page. The numbers live in `_system/studio/blender/vf_standards.py` (and, generated from it, in the
skill's standards table); this page says what they are for. Approved sheets are in `Reference/`.

## Identity
A collection of animal portraits that belong together: every animal seen from the same true-isometric camera, built
from the same size of voxel, lit by the same rig, finished in the same satin plastic, in vivid solid colours, each on
its own soft flat colour. Recognition comes from proportions and three to five species features carried by large
blocks, never from detail. The information artworks speak in a friendly, Duolingo-like voice with chunky cards.

## The picture
| Element | Rule |
|---|---|
| Camera | orthographic, azimuth 45°, elevation 35.264° (true isometric), deep focus |
| Facing | head lower right; the face and the left flank visible together |
| Voxel | 0.1 m; the animal 16–32 voxels long, whatever its real size |
| Geometry | `merged`: flat planes per part, bevelled where the surface turns; parts meet with a seam (approved 2026-11-15) |
| Material | satin plastic (roughness 0.62, thin coat), light subsurface; no texture, no gradient |
| Colour | Khronos PBR Neutral view, neutral slate-100 sky fill: colours render as authored (owner 2026-11-16: "the model colour is so pale" under AgX) |
| Palette | Tailwind v4 tokens; 3–6 keys; large areas shades 50–800, details any shade |
| Background | one Tailwind token per species, shades 50–300, complementary, ΔE ≥ 30 from the main colour; exactly that hex in every open pixel |
| Light | warm key sun front-left and 55° high (`iso_top`, approved 2026-11-15), cool rim behind without its own shadow |
| Shadow | one soft shadow on the ground, strength 0.65, composited over the background |
| Framing | the whole animal, centred; illustrations fill 70 % (1:1), 82 % (9:16 width), 68 % (16:9 height) on the binding side |
| Brand | none in the images |

## Choosing a background
1. Name the animal's main coat colour family (orange fox, grey koala, black-and-white panda).
2. Start from the opposite family (orange ↔ teal/cyan/sky, yellow-amber ↔ violet/indigo, pink ↔ emerald, red ↔ teal);
   for neutral animals pick a soft colour of their world (bamboo lime for the panda, Arctic blue for the polar bear,
   sunny amber for the grey koala).
3. Shade 200 (300 for very light animals); `vf.py check` enforces ΔE ≥ 30; the preview must separate the animal at
   thumbnail size.
4. Write the reason in `animal.json → look.why`. Animals may share a background.

The first ten: fox teal-200, panda lime-200, red panda cyan-200, penguin sky-200, capybara indigo-200, flamingo
emerald-200, koala amber-200, lion violet-200, polar bear blue-300, giraffe sky-300.

## The information artwork (Duolingo-style cards)
| Element | Rule |
|---|---|
| Arrangements | 1:1 header and photo across the top, stat tiles beside the animal, three cards in a bottom band · 9:16 header, the animal with the photo beside it, 2×2 stats, three stacked cards · 16:9 the animal left; header + photo, 2×2 stats, two cards and the fun fact right |
| Cards | white, rounded (1.5u), a darker lip under each (background + 200), 1.4u padding; flat, no gradients or shadows |
| Fun fact | a full-colour card in the background's family at 700 with white type |
| Photo | a real photograph in a white framed card, cropped to fill; credit underneath: `Photo: <author> · <licence>` |
| Status | the IUCN chip in the status colour (LC emerald, NT lime, VU amber, EN orange, CR red) |
| Type | Poppins: kicker Bold caps in a dark pill · name ExtraBold (≤ 2 lines) · scientific name italic · labels Bold tracked caps · values ExtraBold · body Medium · fun fact SemiBold |
| Unit | u = 1 % of the short side |
| Copy | `kicker` (Class · family in plain English), 4 stats (label ≤ 12, value ≤ 11), Home turf ≤ 100, On the menu ≤ 95, one fun fact ≤ 115 characters |
| Voice | short, warm, concrete, a surprising bit first, everyday comparisons, at most one exclamation per card; no AI-slop words (majestic, fascinating, crucial role, truly, delve); hypotheses said as such |
| Fit | type never shrinks; too much text is an error naming the field; numbers stay with their unit when lines wrap |

## Files
`Color/tailwind-v4-palette.json` (copy of Nilant's), `Fonts/` (Poppins, OFL), `Reference/` (approved look sheets:
rig and geometry 2026-11-15, colour fidelity 2026-11-16).
