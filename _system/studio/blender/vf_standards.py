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

STANDARDS_VERSION = "2.2"         # 2.0 (2026-11-16): the bulky, posed blocky-mob look; 2.1: plates off, cards
                                  # redesigned; 2.2 (2026-11-17): the motion (rig and loops) approved
COLLECTION = "Voxel Fauna"

# ---- Voxel geometry ---------------------------------------------------------------------------------------------------
VOXEL = 0.1                  # NEW: metres per voxel. 0.1 m keeps a 24-voxel animal at 2.4 m, the scale Nilant's
                             # metre-based light, bevel and subsurface values were tuned at
BUDGET = (16, 56)            # NEW: the absolute range of an animal's longest side, in voxels (posed). Each animal's own
                             # budget comes from its real size (SIZE_RULE)
# APPROVED by the owner 2026-11-16 (owner: "add more pixel for larger animal, but keep it blocky bulky", then "scale with real
# size"): the longest side follows the species' real longest dimension L (metres, look.size.real_m: nose to tail tip,
# or height for upright and long-necked species) on a gentle curve, target = base x L^exponent, so a 1 m red panda gets 28
# voxels, a 2.8 m lion 42 and a 5 m giraffe 53, and the bigger animal is built from finer blocks. Was one budget for
# every animal (16-32, target 24).
SIZE_RULE = dict(base=28.0, exponent=0.4, tolerance=0.15)


def size_budget(real_m):
    """(min, max, target) voxels on the posed longest side for an animal whose real longest dimension is real_m."""
    target = max(BUDGET[0], min(BUDGET[1], round(SIZE_RULE["base"] * float(real_m) ** SIZE_RULE["exponent"])))
    tol = SIZE_RULE["tolerance"]
    return max(BUDGET[0], round(target * (1 - tol))), min(BUDGET[1], round(target * (1 + tol))), target


# APPROVED by the owner 2026-11-16 (owner: "rotate the section so it looks more dynamic", "subtle tilts, but ... dynamic pose that
# different for every animal based on animal personality"): parts turn at their joints by at most this many degrees
# on any axis; plates (flat surfaces, owner: "look at the flamingo feet") are squashed to PLATE voxel.
# Plates are switched OFF, APPROVED by the owner 2026-11-16 (owner: "disable flat pixel for now, maybe it is exist in future, but not for
# current animals"): every part is made of whole voxels; vf_voxel.plate() stays for later, `vf.py check` refuses it.
POSE = dict(max_angle=40.0, plate=0.2, plates=False)
# The animation rig and its motion (vf_rig.py), APPROVED by the owner 2026-11-17 ("i confirmed all of them, all model is
# good", then "Previews + motion"): an armature from the joints, the sections skinned with rigid weights, looping
# actions from the motion library, each frame grounded on its posed voxels. The numbers that shape the motion:
MOTION = dict(
    fps=24,
    frames=dict(pose=1, idle=48, walk=48, walk_large=64, flap=48, hop=48, swim=32, waddle=48, howl=48, doze=48,
                shake=24, yawn=48, fan=48, reach=48, sniff=48),
    cycles=dict(walk=2, flap=2, hop=2, waddle=2),
                             # v2 (owner 2026-11-17: "really dynamic"): two strides (flaps, hops) a loop, so the head
                             # can look around at half the stride's pace and the loop never feels like a metronome
    large=40,                # posed length (voxels) from which an animal walks with the slower cycle
    leg_swing=26.0,          # degrees each way, a stiff leg (block-game mobs walk on stiff legs); v1 22
    leg_swing_knee=20.0,     # degrees each way, an upper leg with a shin under it; v1 17
    knee_fold=34.0,          # degrees the shin folds back while its leg swings forward
    leg_swing_biped=24.0,    # two legs (birds): degrees each way; v1 20
    knee_fold_biped=45.0,    # two legs: degrees the lower leg folds back on the swing
    hop_height=0.22,         # of the posed length, voxels
    life=dict(look=16.0, look_bias=0.3, tilt=9.0, nod=4.0, ear=14.0, ear_tilt=9.0, tail=10.0, wing=12.0,
              wing_flap=26.0, sway=2.5, roll=2.0),
                             # v2: the life layer on every action (degrees): the head looks around (yaw, biased away
                             # from the camera's side), tilts (roll) and nods; each ear perks and droops on its own
                             # beat; tails wag; folded wings flutter, with one fuller flap a loop; the body sways and
                             # rolls with the stride
    bone=(1.5, 10.0),        # bone display length, voxels
    preview_step=2,          # previews keep every 2nd frame: 12 fps
    preview_scale=0.125,     # of the 4096 px square: 512 px (the LOW profile at half its scale)
)
MIN_FEATURE = 1             # NEW: the smallest feature is one whole voxel (an eye, a claw row); never a sub-voxel
BEVEL = dict(width=0.012, segments=4, profile=0.5)
                             # ADAPTED from nilant_look: Nilant's finish makes a bevel BEVEL_SCALE 0.5 of its modelled
                             # width, at most BEVEL_SHARE 0.18 of the piece's smallest side (0.018 m on a 0.1 m voxel),
                             # within 0.006-0.06 m, 4 segments, round. 0.012 m = 12 % of a voxel: every block reads as
                             # its own moulded cube with a thin highlight on each edge
CULL_HIDDEN = True           # NEW: a voxel with all six neighbours in its own part is never seen and is not built
STACK_BIAS = 2.0             # voxels per stacking level, in the animal pass of the animated loops only: the legs stay
                             # put (level 0), the body is nudged one level towards the camera, every other jointed
                             # section (head, tail, wings, with their ears and muzzles) two. The camera is orthographic,
                             # so nothing moves or changes size on screen; only the depth test changes: where sections
                             # cut into each other as they turn, the body is always drawn over the legs and the head
                             # over the body, instead of the two cutting each other differently every frame (owner
                             # 2026-11-18: the panda's head and legs flickered; "dont resize the legs, just make the leg
                             # always on behind body"). The shadow pass is not nudged (the ground shadow is exact);
                             # stills and masters are single frames and keep their approved look
STACK_LIMBS = ("leg", "shin", "foot", "flipper")   # name stems of the limb sections (level 0, behind the body)
GEOMETRIES = {
    "block": dict(limit="NONE", bevel=True, material="plastic"),
                                         # every voxel its own bevelled cube: the grid shows on every face
    "merged": dict(limit="ANGLE", bevel=True, material="plastic"),
                                         # the faces of one part merge into flat planes, bevelled only where the
                                         # surface turns; parts meet with a visible seam (Nilant modelling: "toys are
                                         # assembled; the joints are part of the look")
    "mob": dict(limit=None, bevel=False, material="matte"),
                                         # blocky-mob look: every part a sharp-edged box (no bevel, flat shading),
                                         # matte, flat solid colours; the face is drawn on the front of the head
}
GEOMETRY = "mob"             # APPROVED by the owner 2026-11-16 after three rounds (owner: "i dont like the current
                             # isometric model. make it have minecraft mobs vibes"; sheets in 03 Design/Reference/
                             # look · 2026-11-16 · *.jpg). Was "merged", APPROVED 2026-11-15 ("block"
                             # drew ~1000 small cubes with a grid on every face); compare sheet in
                             # 03 Design/Reference/look · 2026-11-15 · rig and geometry.png
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
ANIMAL_TONE = dict(knee=0.09, slope=0.5, scale=0.95)
                             # v2 (owner 2026-11-17: "edit all the animal model color to not that vibrant", with a
                             # reference sheet whose brightest faces sit near OKLCH chroma 0.12-0.15): every animal
                             # colour keeps its lightness and hue; its chroma up to `knee` stays, above it only `slope`
                             # of the excess remains, then x `scale`. orange-600 0.217 -> 0.146, blue-600 0.246 -> 0.160,
                             # a brown at 0.09 -> 0.086: the loud colours calm down, the soft ones barely move
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
# NEW (2026-11-16, blocky-mob look): a matte, painted-block finish: no coat, no subsurface (it would glow through the
# sharp box edges), a low specular so each face reads as one flat colour, not a reflection.
MATTE = dict(roughness=0.86, specular=0.3, coat=0.0, coat_roughness=0.2,
             subsurface=0.0, subsurface_scale=0.06, subsurface_radius=(0.8, 0.8, 0.8))
MATERIALS = {"plastic": PLASTIC, "matte": MATTE}
PALETTE_RULE = dict(body=(50, 800), detail=(50, 950))    # NEW: Tailwind v4 shades a species palette may use: large
                                                         # areas 50-800 (a capybara is amber-800), details any shade.
                                                         # 2026-11-16 (owner: "for this project, break from tailwind
                                                         # coloring token"): a colour may also be a hex "#RRGGBB"

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
BACKGROUND_RULE = dict(shades=(50, 300), min_delta_e=30.0, max_chroma=0.07, lightness=(0.85, 0.93), min_lightness=0.8)
                             # NEW: one flat colour per animal, chosen to complement the species palette (opposite hue
                             # family where the species allows), a soft Tailwind shade (50-300) or a hex at least
                             # OKLCH lightness 0.8; the animal's main colour (look.palette, first key) must differ from
                             # the rendered background by at least CIE76 delta E 30.
                             # APPROVED by the owner 2026-11-16 (owner: "the background color is too vibrant, make it slightly
                             # desaturated so the animal more popup", then "keep the background vivid but pastel (not
                             # too vibrant or neon), keep it calm"): the background renders as a vivid pastel of its
                             # colour: OKLCH chroma capped at `max_chroma`, lightness held in `lightness`, hue kept
                             # (teal-200 #96F7E4 -> #AEF1E3; soft tokens such as sky-200 are unchanged); every card
                             # colour drawn from its family gets the same chroma factor. A flat chroma x 0.55 was tried
                             # first and greyed the soft colours

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
    # APPROVED by the owner 2026-11-16 (owner: "edit the infographic card design to more appealing. current design is too lame and
    # boring and have tight spacing, make it breathe"): chunkier cards with roomier padding, wider gutters, a pixel-art
    # icon badge on every heading and stat tile (the voxel look carried into the cards), the photo as a tilted sticker.
    # Was radius 1.5, lip 0.6, pad 1.4, photo frame 0.7, no icons, no tilt.
    radius=2.2, lip=0.9, pad=2.0,               # u: card corner radius, the darker lip under a card, inner padding
    card="white", photo_frame=1.0,              # stat tiles and info cards are white; the photo sits in a white frame
    photo_tilt=-3.0,                            # degrees: the framed photo is pasted like a sticker, tilted a little
    gap=2.2,                                    # u: the gutter between stat tiles
    tile_pad=1.3,                               # u: the inner padding of a stat tile (a compact chip)
    badge_shades=-100,                          # an icon badge on a white card: the background family one step lighter
    lip_steps=200,                              # a card's lip is the background token + 200 (sky-200 -> sky-400)
    fact_shade="700",                           # the fun-fact card: the background family at 700 (lip +200), white type
    status={"LC": "emerald-500", "NT": "lime-500", "VU": "amber-400", "EN": "orange-500", "CR": "red-600",
            "EW": "purple-600", "EX": "stone-900", "DD": "stone-400", "NE": "stone-300"},
    status_names={"LC": "Least Concern", "NT": "Near Threatened", "VU": "Vulnerable", "EN": "Endangered",
                  "CR": "Critically Endangered", "EW": "Extinct in the Wild", "EX": "Extinct",
                  "DD": "Data Deficient", "NE": "Not Evaluated"},
    headings=dict(habitat="Home turf", diet="On the menu", fact="Fun fact!"),
    icons=dict(habitat="house", diet="apple", fact="bulb"),
    # a stat tile's icon, by the first keyword its label contains (else a star)
    stat_icons=(("length", "span"), ("height", "span"), ("shell", "span"), ("shoulder", "span"), ("tail", "span"),
                ("tongue", "span"), ("horn", "span"), ("bill", "span"), ("fang", "span"), ("wingspan", "span"),
                ("weight", "weight"), ("lifespan", "heart"), ("egg", "egg"), ("litter", "egg"), ("bab", "egg"),
                ("young", "egg"), ("pregnan", "egg"), ("speed", "bolt"), ("walk", "bolt"), ("dive", "bolt"),
                ("breath", "bolt")),
    photo_licences=("Public domain", "CC0", "CC BY 2.0", "CC BY 2.5", "CC BY 3.0", "CC BY 4.0"),
)
INFO_LAYOUTS = {
    "1x1": dict(header=(0.06, 0.055, 0.64, 0.27), photo=(0.695, 0.06, 0.935, 0.285),
                stats=(0.06, 0.33, 0.295, 0.705), stats_cols=1,
                cards=[("habitat", (0.06, 0.745, 0.34, 0.945)), ("diet", (0.36, 0.745, 0.64, 0.945)),
                       ("fact", (0.66, 0.745, 0.94, 0.945))],
                size=dict(kicker=1.15, title=6.2, sci=2.3, chip=1.15, label=1.05, value=2.2, heading=1.3,
                          body=1.6, fact=1.65, credit=0.9)),
    "9x16": dict(header=(0.07, 0.035, 0.93, 0.205), photo=(0.645, 0.228, 0.93, 0.39),
                 stats=(0.07, 0.488, 0.93, 0.615), stats_cols=2,
                 cards=[("habitat", (0.07, 0.637, 0.93, 0.738)), ("diet", (0.07, 0.755, 0.93, 0.853)),
                        ("fact", (0.07, 0.87, 0.93, 0.975))],
                 size=dict(kicker=2.0, title=8.8, sci=3.6, chip=2.0, label=1.8, value=3.7, heading=2.1,
                           body=2.45, fact=2.5, credit=1.4)),
    "16x9": dict(header=(0.50, 0.055, 0.785, 0.355), photo=(0.805, 0.065, 0.962, 0.355),
                 stats=(0.50, 0.39, 0.965, 0.62), stats_cols=2,
                 cards=[("habitat", (0.50, 0.65, 0.649, 0.945)), ("diet", (0.658, 0.65, 0.807, 0.945)),
                        ("fact", (0.816, 0.65, 0.965, 0.945))],
                 size=dict(kicker=1.75, title=6.8, sci=3.0, chip=1.75, label=1.45, value=2.7, heading=1.55,
                           body=1.85, fact=1.9, credit=1.25)),
}
INFO_LIMITS = dict(common=22, scientific=34, kicker=30, stats=4, stat_label=12, stat_value=11,
                   habitat=100, diet=95, fact=115, facts=2)
INK_RULE = dict(min_body_contrast=7.0, min_label_contrast=4.5)     # WCAG contrast of type on its own card or ground

# ---- Identity --------------------------------------------------------------------------------------------------------
# Animal code = Nilant's YY-SEQ (26-001 ...). Image ID = VF-<code>-<kind>-<ratio>, e.g. VF-26-001-ILL-1x1.
IMAGE_ID = "VF-{code}-{kind}-{ratio}"
STATUSES = ("Research", "Modelling", "Preview", "Preview approved", "Final", "Registered", "Approved")
