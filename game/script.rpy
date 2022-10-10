# Start
label start:
    jump actOne

#menu debug:
#    "DEBUG: CHOOSE AN ACT"

#    "Act One":
#        jump actOne

#    "Act Two":
#        jump actTwo

#    "Act Three":
#        jump actThree 

label return_actOne:
    if act_two_checked == True:
        jump actThree
    jump actTwo


label return_actTwo:
    if act_one_checked == False:
        scene bg3a with dissolve
        jump ChooseAct_One
    jump actThree

label return_actThree:
    jump ending

label ending:
    scene bg black
    with dissolve

    return