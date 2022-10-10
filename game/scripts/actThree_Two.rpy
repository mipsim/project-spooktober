label actThree_Two:
    # Setup ---------------------------
    scene bg3b with dissolve

    play music "audio/finalchoice.mp3"
    # ----------------------------------
    "The light is blinding at first."
    "A harsh and violent red stains the entire room."
    "My coat pulls away from me, blasted by the enormous force of power coming from the anomaly."
    
    "The sight before me is hard to make out."
    "The beam continously blasts and juts out of the ground."
    "The room has been completely annhilated, with debris scattered everywhere."
    
    "The guests stand aimlessly, their eyes tinted crimson, their faces blank without emotion."
    "They all stare at the light, fixated on its bright allure."

    "I try to shake one of them out of it, to bring them back to reality. But it's no use."
    "They remain incapacitated, thralls to whatever is happening here."

    "And standing right next to the beam, standing only a few feet away from its immense power, is Kellum."
    
    "He turns his head as we inch ever closer, and it's apparent that he is the only one with a resemblance of sentience in the room."
    "The detective makes his move first, pulling out his magic wand from his trench pocket."
    # ----------------------------------
    
    show de_look with easeinleft

    de "Hold it right there!" with vpunch
    de "Detective Korvus of the EEA!"
    de "I need you to stop whatever the hell you're doing, and come with me!"

    show de_look_dark with dissolve
    hide de_look
    "But the request seems to fall on dead ears, as Kellum turns only to look at me."

    show kt_surprised at twoChar_xTwo
    show de_look_dark at twoChar_xOne
    with easeinright

    kt "Professor Lortalia!"
    kt "You don't know how happy I am to see you!"
    kt "You, you'll be able to fix all of this!"
    kt "My journal's right here. Just take it."
    kt "Please, I don't want it anymore!"

    show kt_surprised_dark at twoChar_xTwo with dissolve
    show prop_journal at truecenter with easeintop

    "The notebook is quite obviously torn and tattered."
    "It's been beaten to smitherens, yet some of the pages are still left intact."
    
    hide prop_journal
    with easeoutbottom

    show de_look at twoChar_xOne
    hide kt_surprised_dark
    with dissolve
    hide de_look_dark

    "Opening it, the journal's faded ink seems all but indescipherable."

### START BRANCHING

## Main Branch 1/3
menu choose_pass24:
    "You have no idea how to discern the words and phrases being used in this hectic handwriting."

    "What am I supposed to do with this?":
        jump pass24_a

    "Kellum, what's going on? What happened?":
        jump pass24_b

label pass24_a:
    mc "What am I supposed to do with this?"

    "I point at the half-destroyed piece of literature in my hands."
    "I can't hide the fear in my voice as I question Kellum. My lack of confidence doesn't inspire any in him either."

    hide kt_angry
    hide kt_base
    show kt_surprised at twoChar_xTwo

    kt "What do you mean? You gave me Calpurnia's journal!"
    
    hide kt_surprised
    show kt_angry at twoChar_xTwo

    kt "YOU WERE THE ONE THAT CAUSED THIS!" with vpunch
    kt "IF I'D NEVER LISTENED TO YOU..." with vpunch

    "Detective Korvus stands idly by, watching things unfold from the side."
    "A keen observer, his wand remains primed and ready in his hands."

    $ de_knows = True

    hide kt_angry
    show kt_surprised at twoChar_xTwo

    kt "Oh no. Don't tell me..."
    kt "Did you forget how this all started? Why we're here..."
    kt "Temporary amnesia, perhaps?"

    hide kt_surprised
    show kt_angry at twoChar_xTwo

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
    
    de "Your little presentation shook the entire damn university!" with vpunch
    de "That tremor did quite the number on a variety of different experiments for miles around!"

    hide de_look
    show de_base at twoChar_xOne

    de "Wouldn't be much of a pull to say your beloved professor here was an unfortunate casualty of your dabbling with forbidden literature!"
    
    hide kt_angry
    show kt_surprised at twoChar_xTwo

    kt "You...damnit..."
    kt "This was never supposed to happen."

    hide de_base
    show de_look at twoChar_xOne

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

    "Detective Korvus merely gives a sideways glance."
    "His expression shows a cold and emotionless figure, one devoid of emotion."

    show de_base at twoChar_xOne

    de "Don't you dare think you're out of the woods yet."

    hide de_base
    show de_look at twoChar_xOne

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

    hide kt_surprised
    show kt_base at twoChar_xTwo

    kt "I was proven correct in my initial hypothesis."
    kt "Calpurnia did use enthrallment spells to compell her army to her cause."
    kt "My intial experiment was only meant to target a ferocious and terribly tempered mutt. But as you can see..."

    "Kellum gestures to the crowd of hundreds of people in an elongated stupor before the three of us."
    
    hide kt_base
    show kt_surprised at twoChar_xTwo

    kt "In the end, I failed."
    kt "The spell was too powerful to control properly, and now everyone here is suffering for my hubris."
    kt "I was the one that caused this whole ordeal, and I wish for nothing more than this horrible nightmare to end."

    $ de_sympathetic = True

    jump pass24_2

label pass24_b_notrust:
    hide kt_surprised
    show kt_base at twoChar_xTwo

    kt "Heh..."
    kt "Hahahaha..." with vpunch

    hide kt_base
    show kt_evil at twoChar_xTwo

    kt "HAHAHAHAHAHAHAHA!!!" with vpunch
    kt "Do you take me for some kind of incompetent halfwit!"

    hide kt_evil
    show kt_base at twoChar_xTwo

    kt "Fine, the truth."
    kt "A certain professor of the oh-so prestigious Alteria Academy gave I, Kellum Triar, a spell from the vaults hidden deep beneath the academy."

    $ de_accuses = True

    hide kt_base
    show kt_evil at twoChar_xTwo

    kt "Could you imagine the negligence?"
    kt "The sheer hubris required to give a mere student the notes of one Calpurnia, Deserter of Altunia!"
    kt "It turns out the rumors about the Great Deserter were true."
    kt "Mind-control, enfeeblement, absolute control over the souls of the masses!"
    kt "Her notes were filled with them!"

    hide kt_evil
    show kt_base at twoChar_xTwo

    kt "The Professor knew I could decipher the entries."
    kt "They knew I could perform the ritual, said I could improve upon its base work."
    kt "And look at where we are now...Hundreds of people enthralled..."
    kt "All thanks to their belief in an over-hyped braggadocio..."

    jump pass24_2

label pass24_2:
    kt "And you want to know the worst part?"

    hide kt_base
    show kt_angry at twoChar_xTwo

    kt "I don't know how to reverse any of this. They're stuck, and this damn ritual refuses to dissipate!"
    "There is an obvious anger in his voice and frustration that he has not yet managed out what he's doing."
    "But also beneath that, you hear something else from the braggart...concern..."

    hide de_look
    show de_surprised at twoChar_xOne

    "The Detective turns to face me, disbelief in his eyes."

    hide de_surprised
    show de_base at twoChar_xOne

    de "What, under all the Seven Divides, compelled you to do such a thing?"

    $ route_goingon_checked = True

menu choose_pass24_2:
    de "Giving a no-name teacher's pet something written by the Ender of the Silver Age!"

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

    hide kt_angry
    show kt_surprised at twoChar_xTwo

    "In the red light of the crimson beacon, Kellum's face seems to grow just a shade redder."

    $ kt_hero = kt_hero + 1

    hide de_base
    show de_look at twoChar_xOne

    jump choose_aftergoingon

label pass24_2_b:
    mc "It was wrong for me to believe a student could be trusted with such power. I'm sorry Kellum."
    "I cannot bear to look Kellum in the eyes, barely able to imagine the amount of anguish and sorrow he's had to endure."

    hide kt_angry
    show kt_surprised at twoChar_xTwo

    kt "No, Professor Lortalia, please. There's no need to blame yourself for this."
    kt "No one could have expected such an outcome."

    $ kt_victim = kt_victim + 1

    hide de_base
    show de_look at twoChar_xOne

    jump choose_aftergoingon

label pass24_2_c:
    mc "It was rash of me to trust such a corrupted mind with the academy's most precious secrets."
    "My words come out quickly, yet the dissapointment in my voice echoes throughout The Grand Hall for all to hear."
    kt "Well then, dear professor. I can help make sure that such a mistake never happens again."

    $ kt_villain = kt_villain + 1

    hide de_base
    show de_look at twoChar_xOne

    jump choose_aftergoingon

label pass24_2_d:
    mc "Wish I could tell you Detective, but uh, amnesia, remember?"
    "I point to the side of my head, hoping it helps paint a better picture of my unfortunate predicament."
    de "That was nowhere near the answer I wanted to hear, you lousy good-for-nothing private school babysitter."

    $ de_sympathetic = False

    "I chuckle to myself a little, realizing I finally got underneath the detective's skin."

    hide kt_angry
    show kt_base at twoChar_xTwo

    "Kellum smirks ever so slightly at the outburst."
    "The enthralled audience remains unamused."

    hide de_base
    show de_look at twoChar_xOne

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

    "The detective takes a moment to gather his thoughts, contemplating what must be a number of different variables and outcomes within his mind."
    "With a sigh of contention, the Detective steps forward. Ever so subtlety, he seems to cast a spell that affects the singular culprit."
    "Something in my brain identifies the spell near immediately. A truth cantrip, ensuring Kellum doesn't bother to try and deceive him."

    de "Seems that the both of you have gotten yourselves into quite the conundrum, speaking as an unbiased third party."
    kt "I'm sorry but, do I know you?"
    de "Heh, probably not. But I sure do know a lot about you."
    de "Kellum Triar, best student Alteria Academy has ever seen."
    de "Perfect grades, great looks, charming personality."
    de "No wonder you've been awarded Grand Scholar for a monumental three years running!"

    hide kt_surprised
    show kt_angry at twoChar_xTwo

    kt "Wherever you're going with this, just come out and say it. This little play of yours is getting rather tiresome."
    de "See you ain't one for small talk. Shame, especially since I know so much about ya."
    de "It's surprising how much you can learn about a person from the way they live."
    kt "You went through my dorm room? I swear if you harmed even a single hair on Bo's little head I'll-" with vpunch
    de "I didn't harm your precious dog."
    de "I did, however, come across quite the collection. Items of interest I'd like to ask you about if you'd be so kind."

menu choose_pass25:
    de "I did, however, come across quite the collection. Items of interest I'd like to ask you about if you'd be so kind."

    "Question about the Skill Improvement guide":
        jump choose_pass25a

    "Suspect about the Skill Improvement guide":
        jump choose_pass25b

    "Accuse about the Skill Improvement guide":
        jump choose_pass25c

label choose_pass25a:
    de "Firstly, why did you have Skill Improvement, 7th edition guide proudly displayed for all to see?"
    kt "I don't know who you are Detective, but that book was never meant for MY personal usage."
    kt "I...I was giving out lessons to my underlings. I found one of them cheating, and held onto it for safekeeping."

    $ kt_hero = kt_hero + 1

    hide kt_angry

    jump after_choose_pass25

label choose_pass25b:
    de "Tell me, why would a grade A student like yourself need an illegal text such as a Skill Improvement guide?"
    kt "I'm not as great of a student as I may appear."
    kt "Detective, truth be told, I needed it to stay afloat with my colleagues. I'm not in nearly the same league as them."

    $ kt_victim = kt_victim + 1

    hide kt_angry

    jump after_choose_pass25

label choose_pass25c:
    de "Let's start with your little \"supplementary reading.\" A certain text named Skill Improvement, 7th edition?"
    kt "Well, isn't it obvious? Knowledge is power."

    hide kt_angry
    show kt_base

    kt "And when power gains you nothing but respect and revelry in our world, well then there's no reason not to take it when you can."

    $ kt_villain = kt_villain + 1

    hide kt_base

    jump after_choose_pass25

label after_choose_pass25:
    show kt_surprised at twoChar_xTwo

    kt "Wait how did you... a hex of truthsaying?"

    hide kt_surprised
    show kt_base at twoChar_xTwo

    kt "And I didn't even notice it until now... Clever plan detective."

menu choose_pass25_2:
    kt "And I didn't even notice it until now... Clever plan detective."

    "Question about the Book of Dark Arts":
        jump choose_pass25_2a

    "Suspect about the Book of Dark Arts":
        jump choose_pass25_2b

    "Accuse about the Book of Dark Arts":
        jump choose_pass25_2c

label choose_pass25_2a:
    de "I ain't one to be underestimated. Now, you want to explain that book on the Dark Arts you had? The one about transformations?"

    hide kt_base
    show kt_surprised at twoChar_xTwo

    kt "Please! Don't blame me...It was given to me by a close friend..."
    kt "We thought we could change the world by finally cracking the code for one of Calpurnia's spells..."

    $ kt_hero = kt_hero + 1

    jump after_choose_pass25_2

label choose_pass25_2b:
    de "Comes with practice and hard work, something you'd outta look into."
    de "Second, that little novel of yours, the one on Dark magics and forbidden arts? Why do you have it?"

    hide kt_base
    show kt_surprised at twoChar_xTwo

    kt "Please! Don't blame me..."
    kt "I needed something spectacular for my final Grand Scholar presentation, so I took it."
    kt "I thought I could re-purpose a spell made by Calpurnia herself..."

    $ kt_victim = kt_victim + 1

    jump after_choose_pass25_2

label choose_pass25_2c:
    de "Don't think compliments will get you out of this one."
    de "Now, the Dark Arts book. Explain it."
    de "NOW!" with vpunch
    kt "Heh. Do you mean the one written by the Deserter of Altunia herself?"
    kt "Well, I merely took it while no one was looking. This whole ordeal was merely a minor setback."

    hide kt_base
    show kt_angry at twoChar_xTwo

    kt "Know that I plan on finishing what I started."

    $ kt_villain = kt_villain + 1

    jump after_choose_pass25_2

label after_choose_pass25_2:
    de "As in Calpurnia, Deserter of Altunia? The revolutionary that nearly destroyed our great nation!"
    de "You attempted to recast one of her spells for a glorified talent show?"
    "Kellum doesn't say anything, but he flinches, his pride obviously hurting from the accusatory tone of the Detective."

label ending_branch:
    de "Well then, based on what I gathered, there can really be only one conclusion. To all of this."

    if kt_hero > kt_victim and kt_hero > kt_villain:
        jump good_ending
    else:
        jump bad_endings

label good_ending:
    de "Kid, you obviously got yourself into more than you bargained for. This whole little event should've never happened in the first place."
    de "C'mon, let's figure out just how the hell we need to stop this beam of yours and help save all these poor saps."

    show kt_base at twoChar_xTwo

    "Kellum's face floods with relief. Knowing that he's now in safe hands, his demeanor gets noticeably lax."
    "The detective turns to face me and the kindness in his eyes disappears for a moment."

    hide de_look
    show de_base at twoChar_xOne

    de "Don't think my kindness extends to you, however."
    de "Amnesia or not, you still have plenty of explaining to do. Giving a book of that magnitude to a damn college student?"
    de "What were you thinking?"
    "Detective Korvus shakes his head in disapproval but motions me to come along."
    "I don't bother trying to argue with him, as the guilt still eats away at me."

    hide kt_surprised
    hide kt_angry

    hide de_base
    hide kt_base at twoChar_xTwo
    with easeoutright

    "I soon spend hours studying the incantation as Kellum and The Detective starts herding the enthralled to safe areas of the campus."
    "I try to find out what exactly went wrong, but frankly, Kellum's incantation is damn near perfect."
    "I breathe a sigh of relief, realizing that the way to fix everything is spelled out for us."
    "All that's needed is a long anti-magical seance to be performed, a constant chanting that can surely save everyone affected."
    "Kellum, Detective Korvus, and I begin chanting the proper rites. We go for hours, but time seems to speed by quickly, all three of us continuing in perfect harmony."
    "It could easily be described as glorious if it weren't for all the lives on the line and the stakes at hand."
    "By the crack of dawn, the beam becomes noticeably smaller. Humming more and more quietly. Disappearing."
    "Then we start to hear the bodies, each one falling down one by one, no doubt exhausted by the mind-control."
    "Soon enough, the beam dissipated, just as soon as Detective Korvus's reinforcements manage to arrive. And not a second too soon."

    scene bg3a with dissolve
    play music "audio/investigation.mp3"

    show kt_base at twoChar_xTwo
    show de_look at twoChar_xOne
    with easeinleft

    de "I'm beat. Can go the rest of my life not needing to say \"Hullmonna maltork abi loncoralia\" ever again."
    "He gives a pat on the shoulder of Kellum."
    de "You take care of yourself, Grand Scholar. I best not be seeing you creating any more rifts in the sky or none of that from now on."
    kt "I'll uh, do my best to make you proud, Detective."
    de "That's what I like to hear. Stay out of trouble by not trying to cause any in the first place."
    
    hide de_look
    show de_base at twoChar_xOne

    de "And now, onto you..."
    de "Don't think that this'll be the last time I visit you, Professor Lortalia."

    if de_accuses == True:
        jump good_end_accuse
    else:
        jump good_end_notaccuse

label good_end_accuse:
    de "You most certainly ain't getting out of this scot-free."
    de "Expect a visit in the coming days, and you best prepare a case while you're at it. The Council won't look on you highly after this."

    jump good_end_afteraccuse

label good_end_notaccuse:
    de "Your memory loss is likely in need of addressing, but I know a guy."
    de "They can help you get things straightened out. Won't be the first time I've dealt with amnesia cases before, speaking from firsthand experience."

label good_end_afteraccuse:
    hide de_base with easeoutright

    "With that, the Detective quickly shapeshifts into his aven form, taking a position with his murder."
    "He caws nearly non-stop, likely updating them all on the night he's had."

    show kt_base at truecenter with easeinright
    "Kellum turns to face me. He looks miserable and exhausted, but most of all relieved."

    kt "Well, Professor, there isn't really an easy way to say this but here it goes..."

    hide kt_base
    show kt_surprised
    kt "What in all the Seven Divides were you thinking, entrusting me with such an assignment!!!" with vpunch
    kt "The wasted hours spent studying Calpurnia's different texts and notes ON TOP of the utter carelessness with trusting someone like ME with forbidden knowledge."
    kt "I could've blown up the school! Or gone mad with power! Or worse!"
    kt "But..."

    hide kt_surprised
    show kt_base

    kt "I'd be lying if I said I didn't appreciate the opportunity."
    kt "It really meant a lot to me that you'd entrust such information to someone like me. So thank you."
    kt "I mean, it all went to hell and we're gonna have to figure out a way to restore your memory."
    kt "Along with anything else that may have gone wrong because of this explosion..."
    kt "But hey, it's a new day. There's plenty of time to correct the mistakes of the past, all to hopefully make for a better future."

    "On that, I couldn't have agreed more."

    scene bg0 with dissolve
    "GOOD ENDING"
    $ persistent.good_ending = True
    
    jump actThreeOutro

label bad_endings:
    if kt_villain > kt_victim:
        de "Kellum Triar, you are under arrest for crimes against the country of Altunia for practicing blatant heresy. Come with me now!"
    else:
        de "Kellum Triar, I need to bring you in for further questioning. Please, come with me now."

    hide kt_base
    hide kt_surprised
    show kt_angry at twoChar_xTwo

    "The Detective already has his wand out and brimming with power. If he tries to retaliate, Kellum doesn't stand a chance."
    "But Kellum just stands there, eyeing the Detective up and down."
    "And it's obvious that the young student is foolhardy enough to challenge the veteran."

    kt "I won't let you ruin this for me. I can figure this out, I just need more time."
    "Kellum makes a move for his own wand, preparing to cast a spell, but the Detective is one step ahead of him." with hpunch
    "Korvus is only a syllable or so faster but it's enough to guarantee him the victor unless something happens."

menu intervention:
    "Korvus is only a syllable or so faster but it's enough to guarantee him the victor unless something happens."

    "Intervene":
        jump intervene

    "Let It Happen":
        jump letHappen

label intervene:
    de "-Culto-"

    "I push Korvus at the last possible moment, deflecting his aim to a nearby pillar." with hpunch
    "A bolt of harsh blue lightning strikes the column, lighting the hall for a brief moment before the blow dissipates." with vpunch
    "Before the Detective is able to say anything else, Kellum retaliates, casting the same spell straight at his assailant."

    kt "Elko Vos Cultora!" with vpunch

    hide de_base
    hide de_look
    show de_surprised at twoChar_xOne

    "A bright red thunderbolt flies into the chest of the detective, lighting his body in a horrendous and brutal fashion." with hpunch

    hide de_surprised with easeoutbottom

    "His body convulses, twitching every other moment until his body finally relaxes." with vpunch
    "His eyes roll back into his skull, and his scarf slowly dissipates into the shadows."

    if  kt_villain > kt_victim:
        show kt_angry at truecenter with easeinright

        jump evil_ending
    else:
        show kt_angry at truecenter with easeinright

        jump martyr_ending

label evil_ending:

    hide kt_angry
    show kt_base

    kt "You know, for a moment there, I thought you were going to allow him to kill me."
    kt "But I knew you'd come through in the end Professor Lortalia. Just like you always do."
    kt "So what do you say we finally finish this, and get it over with? See this through to the end."

menu evil_choice:
    kt "So what do you say we finally finish this, and get it over with? See this through to the end."

    "Sure, Kellum.":
        kt "You likely don't remember it, but when you first gave me Calpurnia's journal, I remember vividly saying that I wouldn't disappoint you."
        kt "It's rather cathartic to know that I've kept my word all this time."
        jump evil_ending2

    "What? No! End the spell!":

        hide kt_base
        show kt_evil

        kt "hehehehehehehe...."
        kt "Hahahahahahahahaha! Sorry. It's just..."

        hide kt_evil
        show kt_base

        kt "It's funny that you thought you had a choice in the matter..."

label evil_ending2:
    "With that, Kellum pulls out his wand and utters a single phrase, almost as a whisper."

    hide kt_base
    show kt_angry

    kt "Zentra."
    "My body freezes in place, eyes facing forward so I can only see Kellum and the beacon he's made." with vpunch

    hide kt_angry
    show kt_base

    kt "You know, when we first set out to alter this incantation, to lower its potency to make it more ethical, I never had any real intention of doing any of that."
    kt "What I wanted, what I really wanted, was to push myself."

    hide kt_base
    show kt_evil

    kt "To see just how far I could go without breaking. See if I could cast a spell made by the Mad Betrayer herself. Remake history!"

    "Kellum steps ever closer to the portal, its red hue slowly becoming darker and darker as he proceeds to its torrential arcane potency."

    kt "And lo and behold, it went perfectly. All I needed was time."
    kt "Time for this beacon to harmonize with the surrounding area, so that I could enthrall every living being within the school and the nearby town."

    hide kt_evil
    show kt_angry

    kt "But then you and your little detective friend here just had to try and intervene, had to try and stop me."
    kt "And I mean, well look at where it got him..."

    hide kt_angry
    show kt_base

    kt "But I'll reward your loyalty in the end. At least partially. You cannot say I am not a benevolent ruler."

    hide kt_base
    show kt_evil

    kt "Professor Lortalia, if I should even call you that still, will be the first honorary member to join me in my conquest of Altunia."

    hide kt_evil
    show kt_evildark

    kt "It is my thanks, for helping me start a new era. I would never have gotten here without you."

    hide kt_evildark with easeoutright

    "The beam is now a sickly, opaque black, Kellum steps forward into its jutting beam, and it absorbs him eagerly, pulling him into its eerie darkness." with hpunch
    "The beam moves upwards, circling and spreading over the sky until the light of the moon can no longer be seen." with vpunch

    scene bg0 with dissolve

    "It shades over us and pulsates once, as far as the eye can see. My head rumbles and shakes ever so subtly." with vpunch
    "My thoughts start to become cloudier as HE SAVES US FROM THIS TURGENT HELL THAT IS OUR PUNY MORTALITY." with hpunch
    "No."
    "nonononononononononono"
    "HIS WILL SHALL BE KNOWN ALL ACROSS THE COUNTRY OF ALTUNIA. PRAISE AND BE MERRY FOR HIS COMING IS NIGH." with vpunch
    "no HIS please WILL i IS don't JUST want AND this GOOD." with hpunch
    "MAY LORD TRIAR REIGN MAY LORD TRIAR REIGN MAY LORD TRIAR REIGN MAY LORD TRIAR REIGN MAY LORD TRIAR REIGN help me MAY LORD TRIAR REIGN MAY LORD TRIAR REIGN MAY LORD TRIAR REIGN MAY LORD TRIAR REIGN MAY LORD TRIAR REIGN MAY LORD TRIAR REIGN MAY LORD TRIAR REIGN MAY LORD TRIAR REIGN MAY LORD" with vpunch

    "EVIL ENDING"
    $ persistent.evil_ending = True

    jump actThreeOutro

label martyr_ending:
    hide kt_angry
    show kt_surprised

    kt "I... thank you for saving me, Professor Lortalia."
    kt "But this was unjust on all accords. I shouldn't have killed that man! He... he didn't deserve to die from my mistakes..."
    kt "It's my fault he's dead. It's my fault these poor people have been enthralled. Oh, Seven Divides this was never supposed to happen."

    "Kellum is gripping his head, sobbing tears as he realizes the full extent of his actions..."
    "I walk up to him, and try to console the shaken student with -"

    kt "NO! Don't touch me! I don't deserve kindness or sympathy..." with vpunch
    kt "I'm a damn freak. A monster who dabbled with magic far outside his realm of expertise!"
    kt "And for what? A better grade? A stupid title no one gives a damn about!"
    kt "What was this all for? Why did I make so many people suffer?"

menu martyr_choice:
    kt "What was this all for? Why did I make so many people suffer?"

    "You can still fix this. Fix everything!":
        "No, Professor Lortalia. I can maybe fix the enthrallment, but... not everything else. I can't. It's too much..."
        jump after_martyr_choice

    "...":
        kt "There's only one solution... Only one thing I can think of that can reverse all of this..."

label after_martyr_choice:
    hide kt_surprised
    show kt_base

    kt "Thank you, professor. I... I appreciated everything you taught me."
    hide kt_base with easeoutright

    "Kellum gives one more cheerful smile, before running straight into the red beam, diving in before I can try stopping him."
    "The spell starts to crackle, barely holding its shape together and falling apart at the seams."
    "Booms can be heard emanating from its base, jostling my bones to their core." with hpunch

    scene bg1 with dissolve
    "Suddenly, a blast of white suddenly erupts from the base." with vpunch

    scene bg3a with dissolve
    play music "audio/investigation.mp3"

    "I'm awakened by the shaking of a strong hand against my shoulder. It's a student, seemingly just as dazed and confused as I am."
    "I get my bearings and eventually it upright, only to see a sea of equally confused and bewildered people surrounding me."
    "The sponsors and alumni have seemingly left their stupor, finally autonomous and able to think again."
    "Some of them hug and hold one another."
    "Others cry, realizing the potential danger they were just in and relieved at the realization that they're still alive."
    "Yet with all the commotion, I don't see the one face that really matters. The one face I wanted to save."
    "And no matter how hard I try, Kellum is nowhere to be seen."

    scene bg0 with dissolve
    "MARTYR ENDING"
    $ persistent.martyr_ending = True
    jump actThreeOutro

label letHappen:
    hide de_base
    show de_look at twoChar_xOne

    de "-Cultora!" with vpunch

    hide kt_angry
    show kt_surprised at twoChar_xTwo

    "It takes less than a second for the shot to find its target. It goes through his body in an instant." with hpunch
    "Kellum, wide-eyed, slowly lowers his head to the black smear now adorning his chest. Directly to the heart."
    
    hide kt_surprised with easeoutbottom

    "Kellum crumples to the ground, the glow in his gem slowly fading away." with vpunch
    "He lies motionless on the stage of the theater, dropping face-first on the ground with a sickly thud."
    
    show de_look at truecenter with easeinleft

    "The Detective remains silent for a moment, as he eyes his victim and sits with the knowledge that he has taken a life."
    "It's most likely not his first, and most certainly won't be his last."

    hide de_look
    show de_sus

    de "I'm sorry you had to witness that. I could tell the both of you were close. My condolences."   
    "He can't even look me in the eyes when he says it."
    hide de_sus with easeoutright

    "Slowly, the red beam in the sky starts to disappear, and one by one, each enthralled guest falls to the ground, suddenly regaining consciousness soon after."
    "The Detective begins talking to each of the people affected, corraling them to the proper help and accommodating them however he can."
    "Anything to avoid the dead college student at the stage front."
    "I walk up to the lying body of Kellum, unsure of how to process all of this."
    "On the one hand, he was a student of mine, a gifted prodigy destined for great things, but on the other, he was foolish to even attempt a fight."
    "I just stare at his lifeless body."
    "The worst part is that I can't remember anything about why I liked him, why we were so close, the justification for why I feel so empty seeing him lying there."
    "Was he misguided?"
    "Overambitious?"
    "Sure, but he had talent, heart, and skill. And now all I can do is stand aside and wait."
    "Wait and wonder if I could have done anything to save such a young soul from such a gruesome fate."

    scene bg0 with dissolve
    "BAD ENDING"
    $ persistent.bad_ending = True
    
label actThreeOutro:
    #"DEBUG: End of Act Three"
    jump return_actThree