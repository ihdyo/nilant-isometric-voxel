# Voxel Fauna · Stock Platforms

Where the export package goes, what each platform requires, and how to avoid the usual refusals. Requirements change:
check each platform's contributor page before a big batch. Read on 2026-11-15.

## What we deliver per animal
- The export package (owner, 2026-11-17) in `02 Animals/<code> · <Name>/export/`: two 4096 × 4096 master renders
  (dynamic and regular blocky pose; each crops to 1:1, 9:16 2304×4096 and 16:9 4096×2304), the loop GIF (1080 square) and the A5 card PDFs (English, Indonesian).
- `vf.py stock <code>`: sRGB JPEGs (quality 95, 4:4:4, ICC embedded, XMP title/description/keywords) as `export/VF-<code>-STOCK.jpg` (the whole dynamic master, 4096×4096, 16.8 MP, no crop),
  `05 Publish/Stock/<code> · Adobe Stock.csv` and `· Shutterstock.csv`, and a Gumroad zip of the PNG masters in
  `05 Publish/Gumroad/`.
- No logo, watermark, signature or URL in any image (owner, 2026-11-15).
- Every upload event is recorded with `vf.py log` (the platform's workbook, `05 Publish/Platforms/Voxel Fauna · <Platform>.xlsx`, Publish Log sheet, and `Voxel Fauna · Publish Log.md`).

## The photo on the information artworks (owner, 2026-11-16)
The information artworks carry a real photograph of the species by a third party (public domain, CC0 or CC BY,
credited on the artwork). Stock sites license your content as your own work: Adobe Stock and Shutterstock contributors
must own all rights in what they submit, and third-party photos, even free ones, are a reason for refusal or a later
takedown. So:
- **Stock sites get the stock image only** (`STOCK.jpg`) (`vf.py stock` does this).
- **Gumroad gets the whole package**: selling a design that includes a CC BY photo is allowed with the credit, which
  is printed on the card; public domain and CC0 need none. Keep the licence table of `docs/references.md` in the listing or
  the zip's notes if you want to be thorough.
- If an information artwork should go to a stock site one day, it needs a photograph the owner took (or bought with
  rights to resell inside a design).

## Recommended order
| # | Platform | Why | Upload |
|---|---|---|---|
| 1 | **Adobe Stock** | the owner's target; strong buyer base inside Creative Cloud | the illustrations first (see "similar content") |
| 2 | **Gumroad** | the owner's target; full price, our own licence, bundles | one pack per animal and collection bundles (e.g. 6 or 12 animals) |
| 3 | **Shutterstock** | the largest marketplace, same files as Adobe | the same JPEGs and CSV |
| 4 | **Freepik** (the company renamed itself **Magnific** in April 2026; the contributor site was still `contributor.freepik.com` in a non-official report) | heavy demand for 3D and isometric illustration | verify current rules first |
| 5 | **Creative Market** (or Etsy) | packs like Gumroad, a design-buyer audience | zips |
| 6 | **Dreamstime**, **Vecteezy**, **123RF** | low effort once the JPEGs and CSVs exist | optional, non-exclusive |

Keep everything **non-exclusive** (no exclusive programme such as iStock exclusive) so the same images can be on
every platform and on Gumroad.

## Adobe Stock
- **Illustrations: JPEG, sRGB, 4–100 MP, up to 45 MB** (Adobe's illustration requirements page, updated
  2026-06-11). A separate PNG category takes images with transparent backgrounds; ours are opaque, so JPEG.
- **Metadata:** title up to 200 characters (lead with the subject: "Red Fox (Vulpes vulpes) isometric voxel 3D
  illustration…"); up to 49 keywords, the first 10 weigh most. `vf.py stock` writes both into the JPEG (XMP) and the
  CSV (columns Filename, Title, Keywords, Category, Releases; category 1 = Animals). Upload the JPEGs, then the CSV in
  the Contributor Portal.
- **Generative AI checkbox:** tick "Created using generative AI tools" only when generative AI made or changed the
  primary subject. These images are modelled and rendered in Blender (the model is code, the render is EEVEE): no
  generative image tool is involved, so the box stays unticked. Adobe refuses both unlabelled AI content and
  non-AI content labelled as AI. Contributors report original 3D renders being refused as "AI" by moderation; keep
  the `.blend`, `model.py` and `build.json` as proof of process for an appeal to Contributor Support.
- **Similar content:** Adobe refuses near-duplicates (same subject, small changes of angle, crop or colour). Our three
  illustration ratios of one model are similar by design. Start with **ILL 1:1 and ILL 16:9** per animal
  (`vf.py stock <code> --only ILL-1x1,ILL-16x9`), watch the acceptance rate, then decide on 9:16 and the information
  artworks. Spreading uploads of one animal over different days also helps.
- **Text in images:** the information artworks carry type; spelling must be perfect and every fact true (our sources
  rule), and nothing may name a brand.
- **Property release:** not needed for our own models; some contributors were asked for one on 3D work. If asked,
  answer with the process proof above.

## Shutterstock
- **JPEG (or TIFF without layers), at least 4 MP, highest quality.** JPEG is recommended (everything is converted to
  JPEG on approval).
- Mark uploads as illustrations. `vf.py stock` writes `<code> · Shutterstock.csv` (Filename, Description, Keywords,
  Categories, Illustration, Mature content, Editorial).

## Gumroad
- No technical limits: sell the PNG masters (and optionally the JPEGs) as a zip per animal, plus bundles.
- The brand belongs here: the cover image, the listing text and the licence terms (personal / commercial) are the
  owner's to write; `vf.py stock` only builds the zip of the export package.
- A Gumroad cover is a separate image made for the listing (it may carry the brand); it is not part of the export
  package and not uploaded to stock sites.

## Freepik (Magnific) and the others
Verify before the first upload: accepted formats for 3D/illustration (some take PNG), minimum size, the AI
declaration, the CSV format. Record what you find in the platform's workbook (Read Me) and here (`registry.PLATFORMS` writes the Read Me).

## Sources
- Adobe Stock: [illustration requirements](https://helpx.adobe.com/stock/contributor/submit-your-content/submit-illustrations/technical-legal-requirements-illustration-submission.html),
  [PNG requirements](https://helpx.adobe.com/stock/contributor/submit-your-content/submit-pngs/technical-requirements-png-submission.html),
  [generative AI FAQ](https://helpx.adobe.com/stock/contributor/help/generative-ai-faq.html),
  [common refusal reasons](https://helpx.adobe.com/ee/stock/contributor/content-moderation/common-reasons-content-refusal.html),
  [community: 3D renders refused as AI](https://community.adobe.com/questions-38/my-3d-renders-are-being-rejected-as-ai-what-can-i-do-316740)
- Shutterstock: [technical requirements for images](https://submit.shutterstock.com/help/en/articles/10617390-what-are-the-technical-requirements-for-images),
  [submitting illustrations](https://submit.shutterstock.com/help/en/articles/10594646-how-do-i-submit-illustrations-for-review)
- Freepik/Magnific: [Freepik is now Magnific](https://www.magnific.com/ai/docs/freepik-is-now-magnific)
