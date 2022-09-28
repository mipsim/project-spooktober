# Start
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

label ending:
    scene bg black
    with dissolve

    return