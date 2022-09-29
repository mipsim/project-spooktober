# Characters
define mc = Character("You", color ="#33A9FF")
define de = Character("Detective", color ="#774ec1")
define me = Character("Issac", color ="#D53918")
define st = Character("Stelivia", color ="#D53918")
define hi = DynamicCharacter("hilde_name", color ="#D53918")
define kt = Character("Kellum Triar", color ="#D53918")
define who = Character("???", color ="FFFFFF")

# Sprites
image de_base = "detective_base.png"
image de_base_dark = "detective_base_dark.png"
image me_base = "meethed_base.png"
image me_base_dark = "meethed_base_dark.png"
image st_base = "stelivia_base.png"
image st_base_dark = "stelivia_base_dark.png"
image hi_base = "hilde_base.png"
image hi_base_dark = "hilde_base_dark.png" 
image kt_base = "kellum_base.png"
image kt_base_dark = "kellum_base_dark.png"

# Backgrounds
image bg2a = "bg KellumRoom.png"
image bg3a = "bg hallway.png"
image bg3b = "bg destroyedHall.png"

# Variables
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

## Act Two
default itemBookshelf_checked = False
default itemInk_checked = False
default itemIngredients_checked = False

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

# default ph_date = False

# Animation
transform twoChar_xOne:
    xalign 0.25

transform twoChar_xTwo:
    xalign 0.75