# Characters
define mc = Character("You", color ="#535353")
define de = DynamicCharacter("detective_name", color ="#774ec1")
define me = Character("Issac", color ="#CD9929")
define st = Character("Stelivia", color ="#CD9929")
define hi = DynamicCharacter("hilde_name", color ="#CD9929")
define kt = Character("Kellum Triar", color ="#D53918")
define who = Character("???", color ="FFFFFF")

# Sprites
# Detective
image de_base = "detective_base.png"
image de_base_dark = "detective_base_dark.png"
image de_look = "detective_look.png"
image de_look_dark = "detective_look_dark.png"
image de_surprised = "detective_surprised.png"
image de_surprised_dark = "detective_surprised_dark.png"
image de_sus = "detective_sus.png"
# Issac
image me_base = "issac_base.png"
image me_angry = "issac_angry.png"
image me_sad = "issac_sad.png"
# Stelivia
image st_base = "stelivia_base.png"
image st_look = "stelivia_look.png"
image st_sad = "stelivia_sad.png"
# Hilde
image hi_base = "hilde_base.png"
image hi_happy = "hilde_happy.png"
image hi_bored = "hilde_bored.png"
image hi_uhh = "hilde_uhh.png"
# Kellum
image kt_sil = "kellum_silhouette.png"
image kt_sil_gl = "kellum_silhouette_glow.png"
image kt_base = "kellum_base.png"
image kt_base_dark = "kellum_base_dark.png"
image kt_angry = "kellum_angry.png"
image kt_evil = "kellum_evil.png"
image kt_evildark = "kellum_evildark.png"
image kt_surprised = "kellum_surprised.png"
image kt_surprised_dark = "kellum_surprised_dark.png"

# Backgrounds
image bg0 = "bg black.png"
image bg1 = "bg white.png"
image bg0b = "bg hallway_dark.png"
image bg2a = "bg KellumRoom.png"
image bg3a = "bg hallway.png"
image bg3b = "bg destroyedHall.png"

# Variables
default num_endings = 0
default persistent.good_ending = False
default persistent.evil_ending = False
default persistent.martyr_ending = False
default persistent.bad_ending = False

## Act One
default me_checked = False
default meat_1a_checked = False
default meat_1b_checked = False
default meat_1c_checked = False
default st_checked = False
default hi_checked = False
default hilde_1a_checked = False
default hilde_1b_checked = False
default hilde_1c_checked = False
default hilde_2a_checked = False
default hilde_2b_checked = False
default num_hilde_checked = 4
default act_one_checked = False

## Act Two
default itemBookshelf_checked = False
default itemInk_checked = False
default itemIngredients_checked = False
default act_two_checked = False

## Act Three
default kt_villain = 0
default kt_hero = 0
default kt_victim = 0

default kt_trusting = True
default de_knows = False
default de_accuses = False
default de_sympathetic = False

default route_dowiththis_checked = False
default route_goingon_checked = False
default route_wedonow_chcked = False

# Animation
transform twoChar_xOne:
    xalign 0.25

transform twoChar_xTwo:
    xalign 0.75