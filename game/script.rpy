﻿# Start
label start:
    #jump actOne

menu debug:
    "DEBUG: CHOOSE AN ACT"

    "Act One":
        jump actOne

    "Act Two":
        jump actTwo

    "Act Three":
        jump actThree 

label return_actOne:
    jump actTwo

label return_actTwo:
    jump actThree

label return_actThree:
    jump ending

#DELETEME
#    scene bg temp1
#    with dissolve

#    show kellum_base
#    with easeinbottom

    # play music "audio/---.mp3"

#    kt "Hey there."
#    kt "Are you a witch?"
#    kt "Because you look magical ;^)"

label ending:
    scene bg black
    with dissolve

    return