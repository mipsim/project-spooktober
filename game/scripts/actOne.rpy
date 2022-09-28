label actOne:
    # Setup ---------------------------
    scene bg3a with dissolve

    play music "audio/investigation.mp3"
    # ---------------------------------

    mc "Ugh...my head..."
    mc "Where am I?"

menu actOne_choice1:
    mc "Guess I should look around."

    "Hallway 1":
        jump Meethed

    "Hallway 2":
        jump Stelivia

    "Hallway 3":
        jump Hilde

label returnFromStudent:
    scene bg3a with dissolve

menu actOne_choice2:
    mc "Where to now?"

    "Hallway 1" if me_checked == False:
        jump Meethed

    "Hallway 2" if st_checked == False:
        jump Stelivia

    "Hallway 3" if hi_checked == False:
        jump Hilde

    "We're done here." if me_checked == True and st_checked == True and hi_checked == True:
        jump ActOneOutro

label ActOneOutro:
    jump return_actOne