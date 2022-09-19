label actThree:
    # Setup ---------------------------
    scene bg3a with dissolve

    play music "audio/investigation.mp3"
    # ----------------------------------

    # Opening
    "The sound of my footsteps echo throughout the chambers."
    "Each rising footfall gets me ever closer to The Great Hall."
    "How I even remember it's title, I barely recall."
    "The classrooms, as before, are empty, their doors seeping sadly within their oaken frames, locked tight."

    # Pass 1
    "The night is still."
    "Outside, the silver moon lays bare."
    "Alone, it is unafraid and unphased by any pesty clouds in it's vicinity."
    "The night belongs to it, and it alone."
    "Yet with all the candles being snuffed out, its moonlight glow provides much needed vision for the detective and I."

    # Pass 2
    show de_base with easeinleft

    de "You sure you know where you're going?"
    de "I doubt we have the time to be making any sort of detour."

    # Pass 3
    "I don't even bother giving him a response. I can't afford to waste what breathe I still have."
    "I may not be 100%% just yet, for some reason this university comes to me naturally, as if it were the back of my hand."
    "The turns I make are confident, quick, and sure. This is the right way."

    # Pass 4
    "My cloak flaps along in the breeze. The sweat begins to build on the back of my neck, along the creases of me aged brow."
    "Suprisingly, the detective has kept in pace with me. He of course remains calm and cool."

    # Pass 5
    "But no time to dwell on it now. We're here."

    # Pass 6
    "Finally, I'm here."

    # Pass 7
    "A deep low rumble can be heard from inside."
    "The doors have been blasted open, laying shattered along the marble floors. Their heavy frames lay splintered and broken."
    "They do nothing to hide the red, opaque glow easing out of the Grand Hall."
    
    # Pass 8
    de "You know, you don't have to do this. I can go in there myself, talk some sense into the kid..."

    # Pass 9
    de "Can't promise that he'll see reason, but hey, who knows? Days only been getting crazier by the minute."
    
    jump choose_pass10

# Pass 10
menu choose_pass10:
    de "But just in case anything does happen, I gotta warn you, I'll do what I need to. I'm not looking to see this get any worse than it already has."

    "You will not harm one of my students!":
        jump pass10_a

    "I understand. Do what you need to.":
        jump pass10_b

    "He's a liability now. He must be terminated.":
        jump pass10_c

label pass10_a:
    mc "You will not harm one of my students!" with vpunch
    "The fury in my voice is palpable. And I can tell that it's gotten to the Detective."
    "He jumps for a moment, before settling back down to his gruff demeanor."
    
    de "Hey hey let me make one thing clear. I ain't a murderer."
    de "However. This little student of yours?"
    de "He's been dabbling with things far beyond his control."
    de "Hell, I don't even know if I can stop him at this point..."
    de "And I ain't letting some professor with an amnisiac disorder stop me from saving who I can. End of story."

    jump pass_11

label pass10_b:
    mc "I understand. Do what you need to."

    "I say, with a solemn and grim look on my face."
    "I would hate for the worst to happen, but I am not blind to the turmoil Kellum has caused."
    "The Detective nods his head."
    "The tenseness in his body seems to fade ever so slightly. Relief gained from knowing I won't stop what needs to be done."

    de "I won't hurt him too bad. That's a promise."

    jump pass_11

label pass10_c:
    mc "He's a liability now. He must be terminated."

    "The words come out of my mouth slow and devoid of emotion."
    "They are calculated, precise."
    "It makes the fed flinch ever so slightly."
    "He lets the words hang there, out in the open, until he takes in a deep breath."

    de "Well then. Glad I didn't have you as a professor back when I was studying here..."

    jump pass_11

# Pass 11
label pass_11:
    "With that, he walks forward, pushing open the heavy door."
    
    hide de_base with easeoutright

    "I can only hope that he's really listened to what I said."

    jump actThree_Two

label actThree_Two:
    scene bg3b with dissolve

    # Pass 12
    "The light is blinding at first."
    "A harsh and violent red stains the entire room."
    "My coat pulls away from me, blasted by the enormous force of power coming from the anomaly."
    
    # Pass 13
    "The sight before me is hard to make out."
    "The beam takes center stage, blasting and jutting out of the ground."
    "The room has been completely annhilated, debris scattering everywhere."
    
    # Pass 14
    "The guests stand aimlessly, their eyes blazing with crimson, their faces blank without emotion."
    "They all stare at the light, fixated on it's bright allure."

    # Pass 15
    "I try to shake one of them out of it, to bring them back to reality. But it's no use."
    "They remain incapacitated, thrulls to whatever anomaly is here."

    # Pass 16
    "And standing right next to the beam, standing only a few feet away from it's immense power, is Kellum."
    
    # Pass 17
    "He turns his head as we inch ever closer, and it's apparent that he is the only with a resemblance of sentience in the room."
    "The detective makes his move first, pulling out his magic wand from his trench pocket."
    
    # Pass 18
    show de_base with easeinleft

    de "Hold it right there!" with vpunch
    de "Detective - of the EEA!"
    de "I need you to stop whatever the hell you're doing, and come with me!"

    # Pass 19
    show de_base_dark with dissolve
    hide de_base
    "But the request seems to fall on dead ears, as Kellum turns only to look at me."

    # Pass 20
    show kt_base at twoChar_xTwo
    show de_base_dark at twoChar_xOne
    with easeinright
    kt "Professor Lortalia!"

    # Pass 21
    kt "You don't know how happy I am to see you!"
    kt " You, you'll be able to fix all of this!"

    # Pass 22
    kt "The books right here. Just take it."
    kt "Please, I don't want it anymore!"

    # Pass 23
    # SHOW KELLUM'S JOURNAL AT THIS SPECIFIC POINT
    show kt_base_dark at twoChar_xTwo with dissolve
    show prop_tome at truecenter with easeintop

    "The journal is quite obviously torn and tattered."
    "It's been beaten to smitherens, yet some of the pages are still left intact."
    
    hide prop_tome
    with easeoutbottom

    # Pass 24
    "Opening the pages, they all seem rather indescipherable."
    "You have no idea how to discern the words and phrases being used in this hectic scrall."


label actThreeOutro:
    "DEBUG: Outro"
    jump return_actThree