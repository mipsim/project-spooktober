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

    if persistent.good_ending == True:
        $ num_endings += 1
    if persistent.bad_ending == True:
        $ num_endings += 1
    if persistent.evil_ending == True:
        $ num_endings += 1
    if persistent.martyr_ending == True:
        $ num_endings += 1
    "[num_endings] out of 4 Endings Found"

    return