label actThree:
    # Setup ---------------------------
    scene bg3a with dissolve
    # ----------------------------------

    "The sound of my footsteps echo throughout the chambers."
    "Each step gets me ever closer to The Great Hall."
    "The classrooms are empty, no other student or professor in sight."

    "The night is still."
    "Outside, the silver moon lays bare."
    "Alone, it is unphased by any clouds."
    "Its glow provides much-needed vision for the detective and I."

    show de_base with easeinleft

    de "You sure you know where you're going?"
    de "I doubt we have the time to be making any sort of detour."

    "I don't even bother giving him a response. I can't afford to waste what breathe I still have."
    "I may not be 100%% just yet, but for some reason this university comes to me naturally."
    "This is the right way."

    "My cloak flaps along in the breeze."
    "The sweat begins to build on the back of my neck, along the creases of me aged brow."
    "Suprisingly, the detective keeps in pace with me."
    "He of course remains calm and cool."

    "Finally, I'm here."
    
    de "You know, you don't have to do this."
    de "I can go in there myself, talk some sense into the kid..."

    de "Can't promise that he'll see reason, but hey, who knows?"

    hide de_base
    show de_look

    de "Day's only been getting crazier by the minute."

    hide de_look
    show de_base

    de "But just in case anything does happen, I gotta warn you, I'll do what I need to."
    de "I'm not looking to see this get any worse than it already has."
    
    jump choose_pass10

menu choose_pass10:
    de "I'm not looking to see this get any worse than it already has."

    "You will not harm one of my students!":
        jump pass10_a

    "I understand, but please, don't blame him.":
        jump pass10_b

    "He's a liability now. He must be terminated.":
        jump pass10_c

label pass10_a:
    mc "You will not harm one of my students!" with vpunch

    hide de_base
    show de_surprised

    "The fury in my voice is palpable. And I can tell that it's gotten to the detective."
    "He jumps for a moment, before settling back down to his usual, stand-offish self."
    
    hide de_surprised
    show de_base

    de "Hey hey let me make one thing clear. I ain't a murderer."
    de "However. This little student of yours?"
    de "He's been dabbling with things far beyond his control."

    hide de_base
    show de_sus

    de "Hell, I don't even know if I can stop him at this point..."

    hide de_sus
    show de_base

    de "But I ain't letting some professor with an amnesiac disorder stop me from saving who I can."
    de "End of story."

    $ kt_hero = kt_hero + 1

    jump pass_11

label pass10_b:
    mc "I understand, but please, don't blame him."

    "I say, with a solemn and grim look on my face."
    "I would hate for the worst to happen, but I am not blind to the turmoil Kellum has caused."
    "The detective nods his head."
    "The tenseness in his body seems to fade ever so slightly."
    "Relief gained from knowing I won't stop what needs to be done."

    hide de_base
    show de_sus

    de "I won't hurt him too badly. Can promise you that."

    "The cocky smirk he flashes fails to inspire any sense of trust in his words."

    hide de_sus
    show de_base

    $ kt_victim = kt_victim + 1

    jump pass_11

label pass10_c:
    
    hide de_base
    show de_surprised

    mc "He's a liability now. He must be terminated."

    "The words come out of my mouth slow and devoid of emotion."
    "They are calculated and precise."
    "It makes the fed flinch ever so slightly."
    "He lets the words hang there, out in the open, until he takes in a deep breath."

    hide de_surprised
    show de_base

    de "Well then. Glad we got that sorted then..."

    $ kt_villain = kt_villain + 1

    jump pass_11

label pass_11:
    "With that, he walks forward, pushing open the heavy door."
    
    hide de_base with easeoutright

    "I can only hope that he's really listened to what I said."

    jump actThree_Two