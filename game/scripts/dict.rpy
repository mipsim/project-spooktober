# Characters
define mc = Character("You", color ="#33A9FF")
define kt = Character("Kellum Triar", color ="#D53918")
define de = Character("Detective", color ="#774ec1")
define ms = Character("Meat Sack", color ="#D53918")
define st = Character("Stitch", color ="#D53918")
define bb = Character("Big Brain", color ="#D53918")
define fi = Character("Filbo", color ="#C19F97")

# Backgrounds
image de_base = "detective_temp2.png"
image de_base_dark = "detective_temp2_dark.png"
image kt_base = "kellum_temp.png"
image kt_base_dark = "kellum_temp_dark.png"
image bg2a = "bg KellumRoom.png"
image bg3a = "bg hallway.png"
image bg3b = "bg destroyedHall.png"

# Variables
# Act One

# Act Two
default itemBookshelf_checked = False
default itemInk_checked = False
default itemIngredients_checked = False

# Act Three
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
    xalign -0.1

transform twoChar_xTwo:
    xalign 1.5