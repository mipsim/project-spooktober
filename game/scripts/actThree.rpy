label actThree:
    # Setup ---------------------------
    scene bg3a with dissolve

    play music "audio/investigation.mp3"
    # ----------------------------------

    # Opening
    "The sound of my footsteps echo throughout the chambers."
    "Each rising footfall gets me ever closer to The Great Hall."
    "How I even remember its title, I barely recall."
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
    "The turns I make are confident, quick, and sure."
    "This is the right way."

    # Pass 4
    "My cloak flaps along in the breeze."
    "The sweat begins to build on the back of my neck, along the creases of me aged brow."
    "Suprisingly, the detective has kept in pace with me."
    "He of course remains calm and cool."

    # Pass 5
    "But no time to dwell on it now. We're here."

    # Pass 6
    "Finally, I'm here."

    # Pass 7
    "A deep low rumble can be heard from inside."
    "The doors have been blasted open, laying shattered along the marble floors."
    "Their heavy frames lay splintered and broken."
    "They do nothing to hide the red, opaque glow easing out of the Grand Hall."
    
    # Pass 8
    de "You know, you don't have to do this."
    de "I can go in there myself, talk some sense into the kid..."

    # Pass 9
    de "Can't promise that he'll see reason, but hey, who knows?"
    de "Day's only been getting crazier by the minute."
    
    jump choose_pass10

# Pass 10
menu choose_pass10:
    de "But just in case anything does happen, I gotta warn you, I'll do what I need to. I'm not looking to see this get any worse than it already has."

    "You will not harm one of my students!":
        jump pass10_a

    "I understand, but please, don't blame him.":
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
    de "And I ain't letting some professor with an amnisiac disorder stop me from saving who I can."
    de "End of story."

    $ kt_hero = kt_hero + 1

    jump pass_11

label pass10_b:
    mc "I understand, but please, don't blame him."

    "I say, with a solemn and grim look on my face."
    "I would hate for the worst to happen, but I am not blind to the turmoil Kellum has caused."
    "The Detective nods his head."
    "The tenseness in his body seems to fade ever so slightly."
    "Relief gained from knowing I won't stop what needs to be done."

    de "I won't hurt him too bad. Can promise you that."

    "The cocky smirk he flashes fails to inspire any sense of trust in his words."

    $ kt_victim = kt_victim + 1

    jump pass_11

label pass10_c:
    mc "He's a liability now. He must be terminated."

    "The words come out of my mouth slow and devoid of emotion."
    "They are calculated, precise."
    "It makes the fed flinch ever so slightly."
    "He lets the words hang there, out in the open, until he takes in a deep breath."

    de "Well then. Glad I didn't have {i}you{/i} as a professor back when I was studying here..."

    $ kt_villain = kt_villain + 1

    jump pass_11

# Pass 11
label pass_11:
    "With that, he walks forward, pushing open the heavy door."
    
    hide de_base with easeoutright

    "I can only hope that he's really listened to what I said."

    jump actThree_Two

label actThree_Two:
    scene bg3b with dissolve

    play music "audio/finalchoice.mp3"

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
    "They all stare at the light, fixated on its bright allure."

    # Pass 15
    "I try to shake one of them out of it, to bring them back to reality. But it's no use."
    "They remain incapacitated, thrulls to whatever anomaly is here."

    # Pass 16
    "And standing right next to the beam, standing only a few feet away from it's immense power, is Kellum."
    
    # Pass 17
    "He turns his head as we inch ever closer, and it's apparent that he is the only one with a resemblance of sentience in the room."
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
    kt "The book's right here. Just take it."
    kt "Please, I don't want it anymore!"

    # Pass 23
    # SHOW CALPURNIA'S JOURNAL AT THIS SPECIFIC POINT
    show kt_base_dark at twoChar_xTwo with dissolve
    show prop_journal at truecenter with easeintop

    "The journal is quite obviously torn and tattered."
    "It's been beaten to smitherens, yet some of the pages are still left intact."
    
    hide prop_journal
    with easeoutbottom
    show de_base at twoChar_xOne
    hide kt_base_dark
    with dissolve
    hide de_base_dark

    # Pass 24
    "Opening it, the journal's faded ink seems all but indescipherable."

### START BRANCHING

## Main Branch 1/3
menu choose_pass24:
    "You have no idea how to discern the words and phrases being used in this hectic scrall."

    "What am I supposed to do with this?":
        jump pass24_a

    "Kellum, what's going on? What happened?":
        jump pass24_b

label pass24_a:
    mc "What am I supposed to do with this?"
    kt "What do you mean? You were the one who brought this to me in the first place!"
    kt "This book was given to me by YOU!"
    kt "YOU WERE THE ONE THAT CAUSED THIS!" with vpunch
    "The Detective stands idly by, watching things unfold from the side."
    "A keen observer, his wand remains primed and ready in his hands."

    $ de_knows = True

    mc "Kellum...I don't remember anything..."
    kt "Oh no. Don't tell me..."
    kt "Did you forget how this all started? Why we're here..."
    kt "Temporary amnesia, perhaps?"
    kt "Or maybe some sort of vain attempt to rid yourself of suspicion."

    $ kt_trusting = False
    $ route_dowiththis_checked = True

menu choose_pass24a:
    kt "I must admit Professor Lortalia, you are much more cunning than I once thought..."
    
    "I've really forgotten everything! Your spell was the cause!":
        jump pass24_a_a

    "Kellum, what's going on? What happened?" if route_goingon_checked != True:
        jump pass24_b

    "Okay. Detective, what do we do now?":
        jump pass25

label pass24_a_a:
    mc "I've really forgetten everything! Your spell was the cause!"
    kt "Preposterous! If what I did managed to disturb you so harshly, I couldn't imagine..."
    de "Your little presentation shook the entire damn university!"
    de "That tremor did quite the number on a variety of different experiments for miles around!"
    de "Wouldn't be much of a pull to say your beloved professor here was an unfortunate casualty of your dabbling with forbidden literature!"
    kt "You...damnit..."
    kt "This was never supposed to happen."

    $ kt_trusting = True

menu choose_pass24_a_a:
    "The fire in Kellum's eyes seems to die down, his fury starting to fill with a deep sense of regret."

    "Thank you Detective.":
        jump pass24_a_a_a

    "Kellum, what's going on? What happened?" if route_goingon_checked != True:
        jump pass24_b

    "Okay. Detective, what do we do now?":
        jump pass25

label pass24_a_a_a:
    mc "Thank you Detective."
    "The Detective merely gives a sideways glance."
    "His demeanor shows a cold and emotionless figure, one devoid of emotion."
    de "Don't you dare think you're out of the woods yet."

menu choose_pass24_a_a_a:
    de "You'll be getting your fair shake after this, amnesiac or not."

    "Kellum, what's going on? What happened?" if route_goingon_checked != True:
        jump pass24_b

    "Okay. Detective, what do we do now?":
        jump pass25

## Main Branch 2/3
label pass24_b:
    mc "Kellum, what's going on? What happened?"
    "Kellum stares to the side for a moment, carefully determining what his next words should be."

    if kt_trusting == True:
        jump pass24_b_trust

    if kt_trusting == False:
        jump pass24_b_notrust

label pass24_b_trust:
    kt "All I wanted to do was to be Grand Scholar again..."
    kt "This spell was supposed to be my magnum opus."
    kt "One more lasting hurrah, you would say."
    kt "Something to cement my legacy in the halls of Alteria Academy."
    kt "I was to prove the fables of Calpournia The Mad Blooded were not just works of fiction and ancient Alturnia propaganda!"
    kt "Professor Lortalia entrusted me with deciphering the traitorous mage's notes."
    kt "They said that solving the writing of Calpurnia's spellbook could lead to the final deduction needed to see what compelled people to join her cause."
    kt "I was proven correct in my initial hypothesis."
    kt "Calpurnia did use enthrallment spells to compell her army to her cause. But as you can see before you..."
    kt "My intial experiment was only meant to target a ferocious and terribly tempered mutt. But as you can see..."
    "Kellum gestures to the crowd of hundreds of people in an elongated stupor before the three of us."
    kt "In the end, I failed."
    kt "The spell was too powerful to control properly, and now everyone here is suffering for my hubris."
    kt "I was the one that caused this whole ordeal, and I wish for nothing more than this horrible nightmare to end."

    $ de_sympathetic = True

    jump pass24_2

label pass24_b_notrust:
    kt "Heh..."
    kt "Hahahaha..."
    kt "HAHAHAHAHAHAHAHA!!!" with vpunch
    kt "Do you take me for some kind of incompetent halfwit!"
    kt "Fine, the truth."
    kt "A certain professor of the oh-so prestigious of Alteria Academy gave I, Kellum Triar, a spell from the vaults hidden deep beneath the academy."

    $ de_accuses = True

    kt "Could you imagine the negligence?"
    kt "The sheer hubris required to give a mere student the notes of one Calpurnia, Deserter of Altunia!"
    kt "It turns out the rumors about the Great Deserter were true."
    kt "Mind-control, enfeeblement, absolute control over the souls of the masses!"
    kt "Her notes were filled with them!"
    kt "The Professor knew I could decipher the entries."
    kt "They knew I could perform the ritual, said I could improve upon it's base work."
    kt "And look at where we are now..."
    kt "Hundreds of people enthralled...All thanks to their belief in an over-hyped braggadocio..."

    jump pass24_2

label pass24_2:
    kt "And you want to know the worst part?"
    kt "I don't know how to reverse any of this. They're stuck, and this damn ritual refuses to dissipate!"
    "There is an obvious anger in his voice, frustration that he has not yet managed out what he's doing."
    "But also beneath that, you hear something else from the braggart...concern..."
    "The Detective turns to face me, disbelief in his eyes."

    $ route_goingon_checked = True

menu choose_pass24_2:
    de "What, under all the Seven Divides, compelled you to do such a thing? Giving a no-name teacher's pet something written by the Ender of the Silver Age!"

    "I believed that he could control the spell. My trust in him has yet to waiver.":
        jump pass24_2_a

    "It was wrong for me to believe a student could be trusted with such power. I'm sorry Kellum.":
        jump pass24_2_b

    "It was rash of me to trust such a corrupted mind with the academy's most precious secrets.":
        jump pass24_2_c

    "Wish I could tell you Detective, but uh, amnesia, remember?":
        jump pass24_2_d

label pass24_2_a:
    mc "I believed that he could control the spell. My trust in him has yet to waiver."
    "I say, whole-heartedly believing that Kellum will be able to finish his presentation with a peaceful outcome."
    "In the red light of the crimson beacon, Kellum's face seems to grow just a shade redder."

    $ kt_hero = kt_hero + 1

    jump choose_aftergoingon

label pass24_2_b:
    mc "It was wrong for me to believe a student could be trusted with such power. I'm sorry Kellum."
    "I cannot bear to look Kellum in the eyes, barely able to imagine the amount of anguish and sorrow he's had to endure."
    kt "No, Professor Lortalia, please. There's no need to blame yourself for this."
    kt "No one could have expected such an outcome."

    $ kt_victim = kt_victim + 1

    jump choose_aftergoingon

label pass24_2_c:
    mc "It was rash of me to trust such a corrupted mind with the academy's most precious secrets."
    "My words come out quickly, yet the dissapointment in my voice echoes throughout The Grand Hall for all to hear."
    kt "Well then, dear professor. I can help make sure that such a mistake never happens again."

    $ kt_villain = kt_villain + 1

    jump choose_aftergoingon

label pass24_2_d:
    mc "Wish I could tell you Detective, but uh, amnesia, remember?"
    "I point to the side of my head, hoping it helps paint a better picture of my unfortunate predicament."
    de "That was nowhere near the answer I wanted to hear, you lousy good-for-nothing private school babysitter."

    $ de_sympathetic = False

    "I chuckle to myself a little, realizing I finally got underneath the detective's skin."
    "Kellum smirks ever so slightly at the outburst."
    "The enthralled audience remains unamused."

    jump choose_aftergoingon

menu choose_aftergoingon:
    "..."

    "What am I supposed to do with this?" if route_dowiththis_checked != True:
        jump pass24_a

    "Okay. Detective, what do we do now?":
        jump pass25


## Main Branch 3/3
label pass25:
    "Okay. Detective, what do we do now?"
    "The Detective takes a moment to gather his thoughts, contemplating what must be a number of different variables and outcomes within his mind."
    
    # FIXME PAST THIS POINT =================
    #"Describe the air of uncomfortable tension as The Detective settles into their notes and begins reminscing on what they did."
    #de "Detective chastizes MC, but decides to take the reins and move forward with some plan."
    #kt "Kellum responds sarcastically, as a defense trigger to make sure he doesn't get in more trouble with the Detective."
    #de "Detective addresses Kellum, discussing the pieces of evidence that they found."
    #de "These responses will be based on variables and assumptions made by the player as The Detective in Act 2."
    #de "We can have it only affect three key pieces of evidence, for simplicity's sake."

label actThreeOutro:
    #"DEBUG: End of Act Three"
    jump return_actThree