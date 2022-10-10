label actOne:
    # Setup ---------------------------
    scene bg0 with dissolve

    play music "audio/investigation.mp3"

    $ detective_name = "???"
    # ---------------------------------

    "There is only darkness."
    "This is it. This is everything life has led up to. The nothing at the end of it all."
    "It feels oddly cathartic."
    "The void absorbs me, washing away my fears and woes in its cold embrace."
    "I hope to sink further into the feeling."

    show kt_sil with dissolve
    "But then I see it."
    "The figure is hazy as if it's being seen through a fog of barely recalled dreams."
    "The body is still. Tall, with a set of brown robes and a pair of thick-rimmed glasses framing its face."
    "The figure smiles, face formed into a friendly and inviting grin, one filled with warmth. Trust even."
    "He beckons me to come closer. To greet him."
    "I hesitate, for I do not recognize him, and the void remains ever-consuming."
    "The figure's face contorts."


    show kt_sil_gl with dissolve
    hide kt_sil
    "A small red gem appears on its head, and they begin to glow, a crimson light flooding my vision, assailing my entire being."
    "It burns the darkness away."

    de "Why don'tcha snap out of it already?"
    scene bg1 with hpunch
    hide kt_sil_gl
    "A hard slap across the face stings my right cheek."

    de "You're still breathing and I got some questions that need answerin'. So get up!"

    scene bg1 with hpunch
    "The second slap stings the opposite cheek and jolts me awake."

    scene bg3a with dissolve
    show de_base with easeinleft

    de "Welcome back, Professor. Hope that little nap you had was at least mildly pleasant."

    "A trench-coated man has brought me up to my feet."
    "A number of grey hairs peek out from his brown fedora."
    "He wears a strange black scarf decorated with a crow's face to obscure his mouth."
    "We stand in the middle of an empty classroom. The windows are open, letting in the moonlight to help illuminate our surroundings."
    "They also show a strange obscurity just outside."
    "Peaking just outside of the farthest window, a beam of red light seems to jut out into the sky."
    "A towering beacon of great energy that tints everything near it in a violent scarlet."

    hide de_base
    show de_look

    de "I see you've noticed the big red light coming outside as well."
    de "By your look of confusion, seems like you don't know jack about it."

    hide de_look
    show de_base

    de "Sorry for the rude awakening. Also seems improper to not even introduce myself yet."

    $ detective_name = "Korvus"

    de "Name's Korvus. Detective Korvus, of the EEA."
    de "I came here after I heard reports of an anomaly coming from the campus halls a few hours ago."
    de "I've tried askin' around for advice, but I couldn't find anybody, 'til I happened upon you."
    de "You happen to have a name? Or know what's going on?"

    mc "I can't remember my name. Or anything really..."

    hide de_base
    show de_surprised

    de "Damn...Can't remember anything..."
    
    hide de_surprised
    show de_sus

    de "You may be suffering from some sorta memory loss. Figured as much, since you were knocked silly when I found ya."

    hide de_sus
    show de_base

    de "Considering you don't seem to know what's going on, here's the situation."
    de "Judging by your robes you are, were a professor at Alteria Academy."
    de "It's a fancy-schmancy private college for the magical elite of Altunia."

    hide de_base
    show de_look

    de "Now I never attended this place, but I'm assuming that you folk don't go every day conjuring menacing beams into the sky."
    de "Much less allowing your professors to lose their memories in the middle of a semester."

    hide de_look
    show de_base

    de "Now I know it's asking a lot, but I need you to go around and find some survivors of the blast."
    de "Gather some information as well if you can. The sooner we're both in the loop, the better."

menu actOne_choice1:
    de "Gather some information as well if you can. The sooner we're both in the loop, the better."

    "Why me?":
        jump actOne_choice1a

    "Okay, I'll do it.":
        jump actOne_choice1b

label actOne_choice1a:
    de "Well for one, it'd benefit you greatly to return to being your usual self."
    de "And for another, I'd assume that most witnesses, likely students, will trust you more than some random EEA detective."
    de "It's a mutual benefit for both of us. Means you'll come back to normal sooner and that I'll be getting paid quicker."

label actOne_choice1b:
    mc "Okay, I'll do it."

    "The Detective gives a solemn nod of approval."

    de "Nice to know we're on the same page here."
    de "Go see if you can find anyone else in the area."
    de "Check in on them, ask a couple questions, and see if you can get something useful."
    de "I'll explore the campus a bit more as well."

    hide de_base
    show de_look

    de "Got a lead from a trusted source that there's something of interest on the other side of the campus."
    de "A certain big shot named Kellum Triar..."

    hide de_look
    show de_base

    de "I'll reconvene with you here in an hour or so. See ya soon."

    hide de_base with easeoutright

    "With that. the Detective envelops himself within his scarf, suddenly turning into a small black bird as he flies out an open window."
    "He starts to fly off to the southern end of the college, getting that much closer to the red light, until he veers left towards the student dorms."

    "After he leaves, I take a look down at myself to take a brief inventory."
    "I seem to be wearing a dark purple robe and a long sash of white and gold over my shoulders."
    "Shoulder-length hair blankets itself over my face."
    "I try to scavenge around for a weapon to arm myself with, but unfortunately, there's not much to use."
    "The classroom is empty of anything useful."

    "It was a happy occurrence that the Detective managed to wake me up, but I can't help but wonder if he made the right call."
    "Not to mention not having any idea who the figure in my dream was... or who that person the Detective mentioned is..."
    "But that's beside the point. I make my way toward the exit and decide to do what I can to help."

    "The hallway is seemingly covered head-to-toe in books, all varying in terms of height, heft, and design."
    "Many have fallen to the ground and litter the floor. "

    "Before me, I can really only see three different areas to go to. If only I could understand what the Detective would do in this situation."

menu ChooseAct:
    "Choose who to start investigating as."

    "Play as the Professor":
        jump ChooseAct_One

    "Play as the Detective":
        jump ChooseAct_Two

label ChooseAct_Two:
    "I close my eyes and try to imagine what he'd be doing right now, investigating for possible clues across the college."
    jump actTwo

label ChooseAct_One:
    mc "If I really am a professor, I've got to believe in my own abilities."
    "A scream is heard from one of the rooms."
    "I shake out the thought, realizing that my assistance is needed now."
    "I dash off, trying to find where the scream originated from."

menu actOne_choice2:
    "I dash off, trying to find where the scream originated from."

    "Classroom 1":
        jump Meethed

    "Classroom 2":
        jump Stelivia

    "Classroom 3":
        jump Hilde

label returnFromStudent:
    scene bg3a with dissolve

menu actOne_choice3:
    mc "Where to now?"

    "Classroom 1" if me_checked == False:
        jump Meethed

    "Classroom 2" if st_checked == False:
        jump Stelivia

    "Classroom 3" if hi_checked == False:
        jump Hilde

    "We're done here." if me_checked == True and st_checked == True and hi_checked == True:
        jump ActOneOutro

label ActOneOutro:
    "Guess it's about time to meet with the Detective."
    $ act_one_checked = True
    jump return_actOne