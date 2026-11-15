"""Voxel Fauna · the production standards: every number the collection's look depends on, in one file.

Plain Python (no bpy), so the Blender engine (vf_scene.py) and the command line (scripts/vf.py) read the same values.
These values are fingerprinted in `_system/data/standards.lock.json` (`python _system/studio/scripts/vf.py verify`).
Change one only with a reason, show the owner before/after stills, and relock after the OK:
`python _system/studio/scripts/vf.py lock "what and why"` (it logs a row in `_system/log/DECISIONS.md`).

Provenance: values marked NILANT are copied from the Nilant engine (`A:/WORK!!/_startup/Nilant/_system/studio/blender/`:
nilant_stage.py, nilant_kit.render_setup, nilant_farm.pro_light, nilant_look.py, intro_overhaul.polish_set,
nilant_takes.LENSES["iso"]) as read on 2026-11-15. Values marked ADAPTED change a Nilant value for still images, with
the reason beside them. Values marked NEW have no Nilant equivalent.
"""

STANDARDS_VERSION = "1.0"
COLLECTION = "Voxel Fauna"

# ---- Voxel geometry ---------------------------------------------------------------------------------------------------
VOXEL = 0.1                  # NEW: metres per voxel. 0.1 m keeps a 24-voxel animal at 2.4 m, the scale Nilant's
                             # metre-based light, bevel and subsurface values were tuned at
BUDGET = (16, 32)            # NEW: an animal's longest side, in voxels (min, max). Target 24. Same budget for a mouse
                             # and an elephant: this is a collection of portraits, not a size chart
MIN_FEATURE = 1              # NEW: the smallest feature is one whole voxel (an eye, a claw row); never a sub-voxel
BEVEL = dict(width=0.012, segments=4, profile=0.5)
                             # ADAPTED from nilant_look: Nilant's finish makes a bevel BEVEL_SCALE 0.5 of its modelled
                             # width, at most BEVEL_SHARE 0.18 of the piece's smallest side (0.018 m on a 0.1 m voxel),
                             # within 0.006-0.06 m, 4 segments, round. 0.012 m = 12 % of a voxel: every block reads as
                             # its own moulded cube with a thin highlight on each edge
CULL_HIDDEN = True           # NEW: a voxel with all six neighbours filled is never seen and is not built
GEOMETRIES = {
    "block": dict(limit="NONE"),         # every voxel its own bevelled cube: the grid shows on every face
    "merged": dict(limit="ANGLE"),       # the faces of one part merge into flat planes, bevelled only where the
                                         # surface turns; parts meet with a visible seam (Nilant modelling: "toys are
                                         # assembled; the joints are part of the look")
}
GEOMETRY = "merged"          # APPROVED by the owner 2026-11-15: "block" drew ~1000 small cubes with a grid on every
                             # face, which the brief rules out ("excessive small blocks, noisy geometry");
                             # compare sheet in 03 Design/Reference/look · 2026-11-15 · rig and geometry.png
BEVEL_ANGLE = 30.0           # degrees: "merged" bevels only edges sharper than this

# ---- Camera (three-quarter isometric) -----------------------------------------------------------------------------------
CAMERA = dict(
    type="ORTHO",            # NILANT: the `iso` lens is orthographic and deep-focus ("a diagram you could hold")
    azimuth=45.0,            # NEW: degrees, Nilant's pose convention (0 = in front at -Y; 45 = front-right, at +X -Y)
    elevation=35.264,        # NEW: true isometric, atan(1/sqrt(2)): the three visible faces are foreshortened equally
    distance=40.0,           # metres back from the subject along the view (orthographic: only clipping depends on it)
    clip_start=0.1,
    clip_end=200.0,
    dof=False,               # NILANT: iso = deep focus, everything sharp
)
FACING = "+X"                # NEW: every animal is modelled with its head towards +X and its back up (+Z), its left
                             # side at -Y. Through the camera the head is lower right and we see the front and the
                             # left flank together. Mirroring a species needs the owner's approval

# ---- Light rig ----------------------------------------------------------------------------------------------------------
# ADAPTED (owner, 2026-11-16: "the model colour is so pale"): Nilant's AgX Base Contrast + blue-300 sky turned
# orange-400 (255,137,4) into a dull (197,118,59) on the lit top face, and cream orange-50 into grey. Khronos PBR
# Neutral is the view transform made to show base colours as authored (product renders), and a neutral fill stops
# the blue sky greying warm colours: the same face renders (241,123,40). Compare sheet:
# 03 Design/Reference/look · 2026-11-16 · colour fidelity.png. Nilant's values were AgX/"AgX - Base Contrast", blue-300.
COLOR = dict(view="Khronos PBR Neutral", look="None", exposure=0.0)
SKY = dict(token="slate-100", strength=0.5)
SUN_MIN_ANGLE = 0.12         # NILANT: intro_overhaul.polish_set widens every sun to at least 0.12 rad for soft edges
RIG_TURN = 45.0              # ADAPTED: Nilant's suns are fixed for cameras looking from -Y (azimuth 0); the rig turns
                             # with our camera (azimuth 45) so the key stays front-left of it, as Nilant intends

# Rigs: euler XYZ in degrees before RIG_TURN. "nilant" is pro_light() exactly (key 24 deg above the horizon).
# "iso_top" is a proposal for the owner (key raised to 55 deg so the top faces, which the isometric camera sees, are
# the brightest and shadows stay under the animal). Only the rig named in RIG is used for production.
RIGS = {
    "nilant": dict(
        key=dict(token="orange-200", energy=2.4, rotation=(66.0, 0.0, -50.0), shadow=True),
        rim=dict(token="indigo-200", energy=2.4 * 0.3, rotation=(62.0, 0.0, 140.0), shadow=True),
    ),
    # proposal: the key 55 deg high, and the rim lights edges without casting a second shadow towards the camera
    "iso_top": dict(
        key=dict(token="orange-200", energy=2.4, rotation=(35.0, 0.0, -50.0), shadow=True),
        rim=dict(token="indigo-200", energy=2.4 * 0.3, rotation=(62.0, 0.0, 140.0), shadow=False),
    ),
}
RIG = "iso_top"              # APPROVED by the owner 2026-11-15: with "nilant" the 24 deg key threw a
                             # shadow 2.25x the animal's height off the frame and the rim threw a second one towards
                             # the camera; Nilant's cameras look across a set, ours looks down on the top faces

# ---- Materials ----------------------------------------------------------------------------------------------------------
# NILANT satin plastic (nilant_look.plastic clamps nilant_kit.mat's 0.85 into ROUGH (0.5, 0.62) -> 0.62), with
# subsurface as on Nilant's creatures (nilant_look.skin). ADAPTED: Nilant's "Bare Bones" block texture is left out:
# the brief asks for soft, solid colours with no textures.
PLASTIC = dict(roughness=0.62, specular=0.5, coat=0.08, coat_roughness=0.2,
               subsurface=0.1, subsurface_scale=0.06, subsurface_radius=(0.8, 0.8, 0.8))
PALETTE_RULE = dict(body=(50, 800), detail=(50, 950))    # NEW: Tailwind v4 shades a species palette may use: large
                                                         # areas 50-800 (a capybara is amber-800), details any shade

# ---- Background and shadow (composited) ---------------------------------------------------------------------------------
# NEW. EEVEE has no shadow catcher, and a lit ground under this rig in AgX cannot reach a pastel colour (a white
# ground renders at about RGB 170,175,184). So every image is two EEVEE passes laid over the exact background hex:
#   animal pass   the ground is a holdout, film transparent, AgX: the lit animal with clean anti-aliased alpha
#   shadow pass   the animal is a holdout (still casts shadows and contact occlusion), the ground is a plain diffuse
#                 grey, view transform Standard: the ground's light, so shadow = light / unshadowed light per channel
#   composite     background = hex x (1 - SHADOW.strength x (1 - shadow)) in linear light; the animal over it
SHADOW = dict(strength=0.65,      # how dark a full shadow gets (0 = no shadow, 1 = as the light says)
              deadzone=0.03,      # darkening below 3 % (sampling noise, falloff at the frame edge) is open background:
                                  # exactly the hex. Above it the shadow ramps on continuously (no contour step)
              smooth=0.004,       # the shadow factor is box-blurred twice over this share of the short side first
              ground_grey=0.25,   # albedo of the shadow-pass ground (keeps its light below 1.0 so nothing clips)
              ground_size=400.0)  # metres
BACKGROUND_RULE = dict(shades=(50, 300), min_delta_e=30.0)
                             # NEW: one flat Tailwind token per animal, a soft shade (50-300), chosen to complement
                             # the species palette (opposite hue family where the species allows); the animal's main
                             # colour (look.palette, first key) must differ from it by at least CIE76 delta E 30

# ---- Render profiles ----------------------------------------------------------------------------------------------------
# Shared base (NILANT nilant_kit.render_setup): EEVEE, ray tracing, horizon-scan GI for contact occlusion.
RENDER_BASE = dict(
    engine="BLENDER_EEVEE",
    eevee=dict(use_raytracing=True, use_shadows=True, use_fast_gi=True, fast_gi_method="GLOBAL_ILLUMINATION",
               fast_gi_quality=0.75, fast_gi_step_count=12, fast_gi_ray_count=3, fast_gi_thickness_near=0.3,
               fast_gi_bias=0.02, fast_gi_distance=0.0),
    motion_blur=False,       # ADAPTED: Nilant ultra blurs at a quarter shutter for 60 fps footage; stills have no motion
    bloom=False,             # ADAPTED: Nilant's bloom (nilant_stage.lens, Glare threshold 1.5) only catches emitters;
                             # this collection has none, and a glare node on a transparent film corrupts alpha edges
    file="PNG", color_depth="8",
)
PROFILES = {
    # ULTRA = NILANT film_quality() for a still: same shadow rays/steps, full-resolution ray tracing with denoise,
    # shadow resolution 1.0, light threshold 0.001, full-res fast GI. ADAPTED samples 64 -> 256: Nilant pays 64 per frame
    # because a take is 720 frames; a still pays for one frame, and soft sun shadows and GI keep converging past 64.
    # shadow_samples: the shadow pass only feeds a factor that is blurred over ~16 px at 4096 (SHADOW.smooth), so it
    # keeps Nilant's own 64; measured on the RTX 3050 4 GB at 4096x4096: animal pass 3.8 min, shadow pass at 256 3.1 min
    "ULTRA": dict(scale=1.0, eevee=dict(taa_render_samples=256, shadow_ray_count=4, shadow_step_count=16,
                                        shadow_resolution_scale=1.0, light_threshold=0.001, fast_gi_resolution="1"),
                  rt_resolution="1", rt_denoise=True, shadow_samples=64,
                  estimate={"1x1": 300, "9x16": 90, "16x9": 90}),      # seconds per composition on the RTX 3050
    # LOW = NILANT review_quality(): Nilant's still-review profile (its 270x480 low profile is for timing video only).
    # 8 samples, one shadow ray of 2 steps, ray tracing at quarter resolution (kept on for contact occlusion), at a
    # quarter of the final size. Same scene, model, materials, light and framing as ULTRA.
    "LOW": dict(scale=0.25, eevee=dict(taa_render_samples=8, shadow_ray_count=1, shadow_step_count=2,
                                       shadow_resolution_scale=1.0, light_threshold=0.01, fast_gi_resolution="2"),
                rt_resolution="4", rt_denoise=True, shadow_samples=8,
                estimate={"1x1": 2, "9x16": 1, "16x9": 1}),
}

# ---- Output sizes and compositions ---------------------------------------------------------------------------------------
# Owner (2026-11-15): 4096 px on the long side. 9.4-16.8 MP: inside Adobe Stock's 4-100 MP, Shutterstock's 4 MP minimum.
SIZES = {"1x1": (4096, 4096), "9x16": (2304, 4096), "16x9": (4096, 2304)}
RATIOS = ("1x1", "9x16", "16x9")
KINDS = {"ILL": "Illustration", "INF": "Information"}

# Where the animal sits: `zone` in frame fractions (x0, y0, x1, y1), y down from the top; the animal's projected box
# is centred in the zone and fills `fill` of it on the binding side. Illustrations are centred with balanced space;
# information artworks keep room for the type (layouts in INFO_LAYOUTS).
FRAMING = {
    "ILL": {"1x1": dict(zone=(0.0, 0.0, 1.0, 1.0), fill=0.70),
            "9x16": dict(zone=(0.0, 0.0, 1.0, 1.0), fill=0.82),
            "16x9": dict(zone=(0.0, 0.0, 1.0, 1.0), fill=0.68)},
    "INF": {"1x1": dict(zone=(0.31, 0.32, 0.97, 0.71), fill=0.94),
            "9x16": dict(zone=(0.03, 0.215, 0.62, 0.475), fill=0.94),
            "16x9": dict(zone=(0.02, 0.08, 0.48, 0.95), fill=0.90)},
}

# ---- Information artwork (Duolingo-style card system) ----------------------------------------------------------------------
# Owner (2026-11-16): "edit it like the duolingo style so it more appealing" and "provide the real photo of the animal
# on the animal's infograph". One system in three arrangements (never a crop of another): chunky rounded cards with a
# darker "lip" under them (flat, no gradients, no shadows), white stat tiles, a bold full-colour fun-fact card, an
# IUCN chip in the status colour, and a real photograph in a framed card with its credit. Units: u = 1 % of the
# frame's short side; boxes in frame fractions (x0, y0, x1, y1). Type never shrinks to fit: too much text is an error
# naming the field to shorten. Copy rules (voice) are in the skill, section 5.
TYPE = dict(display="Poppins-ExtraBold.ttf", heading="Poppins-Bold.ttf", body="Poppins-Medium.ttf",
            value="Poppins-ExtraBold.ttf", label="Poppins-Bold.ttf", italic="Poppins-MediumItalic.ttf",
            italic_fallback="Poppins-Medium.ttf", fact="Poppins-SemiBold.ttf", faux_italic_shear=0.2,
            tracking=0.1, leading=1.36)
INFO_STYLE = dict(
    radius=1.5, lip=0.6, pad=1.4,               # u: card corner radius, the darker lip under a card, inner padding
    card="white", photo_frame=0.7,              # stat tiles and info cards are white; the photo sits in a white frame
    lip_steps=200,                              # a card's lip is the background token + 200 (sky-200 -> sky-400)
    fact_shade="700",                           # the fun-fact card: the background family at 700 (lip +200), white type
    status={"LC": "emerald-500", "NT": "lime-500", "VU": "amber-400", "EN": "orange-500", "CR": "red-600",
            "EW": "purple-600", "EX": "stone-900", "DD": "stone-400", "NE": "stone-300"},
    status_names={"LC": "Least Concern", "NT": "Near Threatened", "VU": "Vulnerable", "EN": "Endangered",
                  "CR": "Critically Endangered", "EW": "Extinct in the Wild", "EX": "Extinct",
                  "DD": "Data Deficient", "NE": "Not Evaluated"},
    headings=dict(habitat="Home turf", diet="On the menu", fact="Fun fact!"),
    photo_licences=("Public domain", "CC0", "CC BY 2.0", "CC BY 2.5", "CC BY 3.0", "CC BY 4.0"),
)
INFO_LAYOUTS = {
    "1x1": dict(header=(0.06, 0.05, 0.64, 0.27), photo=(0.70, 0.05, 0.94, 0.29),
                stats=(0.06, 0.32, 0.29, 0.71), stats_cols=1,
                cards=[("habitat", (0.06, 0.755, 0.355, 0.95)), ("diet", (0.37, 0.755, 0.645, 0.95)),
                       ("fact", (0.66, 0.755, 0.94, 0.95))],
                size=dict(kicker=1.15, title=6.2, sci=2.3, chip=1.15, label=1.1, value=2.3, heading=1.4,
                          body=1.72, fact=1.75, credit=0.9)),
    "9x16": dict(header=(0.07, 0.03, 0.93, 0.205), photo=(0.64, 0.225, 0.935, 0.39),
                 stats=(0.07, 0.49, 0.93, 0.635), stats_cols=2,
                 cards=[("habitat", (0.07, 0.652, 0.93, 0.755)), ("diet", (0.07, 0.765, 0.93, 0.855)),
                        ("fact", (0.07, 0.865, 0.93, 0.975))],
                 size=dict(kicker=2.0, title=8.8, sci=3.6, chip=2.0, label=1.9, value=4.0, heading=2.3,
                           body=2.65, fact=2.7, credit=1.4)),
    "16x9": dict(header=(0.50, 0.06, 0.775, 0.36), photo=(0.79, 0.06, 0.965, 0.36),
                 stats=(0.50, 0.39, 0.965, 0.60), stats_cols=2,
                 cards=[("habitat", (0.50, 0.625, 0.728, 0.83)), ("diet", (0.737, 0.625, 0.965, 0.83)),
                        ("fact", (0.50, 0.845, 0.965, 0.97))],
                 size=dict(kicker=1.75, title=7.0, sci=3.0, chip=1.75, label=1.6, value=3.0, heading=1.9,
                           body=2.2, fact=2.3, credit=1.25)),
}
INFO_LIMITS = dict(common=22, scientific=34, kicker=30, stats=4, stat_label=12, stat_value=11,
                   habitat=100, diet=95, fact=115, facts=2)
INK_RULE = dict(min_body_contrast=7.0, min_label_contrast=4.5)     # WCAG contrast of type on its own card or ground

# ---- Identity --------------------------------------------------------------------------------------------------------
# Animal code = Nilant's YY-SEQ (26-001 ...). Image ID = VF-<code>-<kind>-<ratio>, e.g. VF-26-001-ILL-1x1.
IMAGE_ID = "VF-{code}-{kind}-{ratio}"
STATUSES = ("Research", "Modelling", "Preview", "Preview approved", "Final", "Registered", "Approved")
