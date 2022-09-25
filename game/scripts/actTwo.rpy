label actTwo:
    # Setup ---------------------------
    scene bg2a with dissolve

    show de_base with easeinleft

    play music "audio/investigation.mp3"
    # ---------------------------------

    de "So this is the room in question..."
    de "Smells like wet dog, but otherwise it seems about par for the course."
    de "In fact, it's rather tidy given the current state of the university."
    de "Let's start by taking a look around."

menu choose_item:
    de "What should I look at?"

    "Bookshelf" if itemBookshelf_checked != True:
        jump item_bookshelf

    "Spilled ink" if itemInk_checked != True:
        jump item_ink

    "Ingredients on table" if itemIngredients_checked != True:
        jump item_ingredients1

    "Ingredients on table?" if itemInk_checked == True and itemIngredients_checked == True:
        jump item_ingredients2


label item_bookshelf:
    de "Let's see, anything interesting?"
    de "\"Legal History of Transmogrification\""
    de "\"Counter Inductive Spell Structures for Undergrads\""
    de "\"Notes on the Use of Spark Spells in General Combat.\""
    de "Decent study material, but none of it is particularly relevant to the case at hand."
    de "Hmmm...this one seems interesting."
    de "\"Caster in the Rye\""
    de "It was required reading at my magic school, but I can't imagine it's part of any modern curriculum."
    de "Not that it means anything on its own, but let's just hope he doesn't identify with the main character too much."
    de "Ah, here's something different!"
    de "\"Skill Improvement 7th edition.\""
    de "These books are supposed to be banned from university."
    de "They use enchanted ink to automatically improve your magical aptitude."
    de "Useful for improving worker productivity, but it doesn't transfer any base knowledge of how the magic works."

menu de_choice1:
    de "Now why would Kellum have something like this?"

    "He must have been trying to cheat on his exams.":
        jump de_choice1_a

    "He probably got it to give to another student.":
        jump de_choice1_b

    "Maybe he isn't actually as smart as everyone is saying?":
        jump de_choice1_c

label de_choice1_a:
    de "In the hands of an amateur, books like this will only cause undue suspicion."
    de "When paired with someone who knows exactly what they're doing, he could push his abilities far past their limits."
    de "And it doesn't hurt that he would get academic recognition in the process."

    $ kt_villain = kt_villain + 1
    jump end_bookshelf

label de_choice1_b:
    de "It would only take a couple questions to expose Kellum for using something like this."
    de "There's no way he would risk it himself."
    de "Perhaps he gave this book to someone else to help them with their studies."

    $ kt_hero = kt_hero + 1
    jump end_bookshelf

label de_choice1_c:
    de "Perhaps the cult of personality around him has gotten out of hand."
    de "Maybe he never was as smart as they said."
    de "I would be surprised that he lasted this long."
    de "But I guess it benefits no one at this university to reveal their best student as a fraud."

    $ kt_victim = kt_victim + 1
    jump end_bookshelf

label end_bookshelf:
    $ itemBookshelf_checked = True
    jump choose_item

label item_ink:    
    de "Spilled ink on the table, a classic question of causality."
    de "Of all the thousands of possible actions, not to mention the addition of spells, incantations, imbibements, enchantments and all the rest."
    de "Out of all of those I have to narrow it down to a single..."
    
    #"-- Display Paw Print"    
    show de_base_dark with dissolve
    show prop_pawprints at truecenter with easeintop

    de "Oh, it seems he has a dog."

    hide prop_pawprints with easeoutbottom
    hide de_base_dark with dissolve

    de "Well, I guess not everything has to be an enigma."
    de "It seems this ferocious beast has left a trail all the way back to its den: the lower cubby of the autobiography section."
    "-- Opens cubby"
    "-- Dog growls"
    de "Well met familiar, may I ask what you're sitting on?"
    "-- Dog growls again"
    de "I see."
    de "Well I won't make any headway with you by just asking nicely."
    
    #"-- Shows cans of empty dog food 'Curio Brand Dog Food.'"
    show de_base_dark with dissolve
    show prop_canempty at truecenter with easeintop
    
    de "Maybe if I can find a can that isn't empty he'll open up to me."

    hide prop_canempty with easeoutbottom
    hide de_base_dark with dissolve

    $ itemInk_checked = True
    jump choose_item

label item_ingredients1:

    #"-- Display ingredients"
    show de_base_dark with dissolve
    show prop_ingredients at truecenter with easeintop

    de "Ingredients it seems, and not the kind you cook with."
    
    hide prop_ingredients with easeoutbottom
    show prop_cancerb at truecenter with easeintop

    de "Well, I supposed you could cook with this one."
    #"-- Shows dog food 'Cerberus Chum'"

    de "But the rest are \"medicinal\" at best."

    hide prop_cancerb with easeoutbottom
    show prop_ingredients at truecenter with easeintop

    de "Let's see here, dogwart, milliweed, griffin's tongue, and snail urine."
    de "All mainstays in the wizarding pharmaceutical industry, but not exactly household names."

    hide prop_ingredients with easeoutbottom
    hide de_base_dark with dissolve

    de "Not that they are hard to get your hands on."
    de "They can all be extracted from stuff you can get over the counter at any wizard clinic worth its summoning salt."

    $ itemIngredients_checked = True

    if itemInk_checked == True:
        jump item_ingredients2
    else:
        jump choose_item

label item_ingredients2:
    #"-- Shows dog food 'Cerberus Chum'"
    show de_base_dark with dissolve
    show prop_cancerb at truecenter with easeintop

    de "Well I bet I can get that dog to hand over the book he’s protecting with a little state sponsored bribery."
    
    "-- Fills bowl with food"
    hide prop_cancerb with easeoutbottom
    hide de_base_dark with dissolve
    de "Here buddy, don’t you want some food?"
    "-- Dog growls"
    de "Huh, I guess he only eats the good stuff."
    de "Let's see what we can do for the spoiled mutt."
    "-- Closes the Cubby"
    de "Just a quick little swap...and we are good to go."
    
    #-- Show a sloppily filled can of Curio
    show de_base_dark with dissolve
    show prop_canfull at truecenter with easeintop

    de "Alright, I got you the good stuff this time."
    de "You like Curio don't you?"
    de "Look I got a fresh new can of it for you"
    "-- Dog is excited"

    #-- Show filled food bowl
    hide prop_canfull with easeoutbottom
    show prop_bowlfull at truecenter with easeintop
    "-- Dog eats it excitedly"
    hide prop_bowlfull with easeoutbottom
    hide de_base_dark with dissolve

    de "Perfect, and if you don't mind I'm going to borrow this dog bed from you."
    de "Doesn't look particularly comfortable anyhow."
    
    #"-- Show journal"
    show de_base_dark with dissolve
    show prop_tome at truecenter with easeintop

    de "Well I'll be, I believe we found the smoking wand."
    hide prop_tome with easeoutbottom
    hide de_base_dark with dissolve

    de "Dark Arts, Summoning Demons, Transforming Flesh, etc. etc."
    de "Not the kind of stuff you get into freshman year."
    de "These are some real \"I knew them before they were cool\" type spells."
    de "He would need access to some seriously twisted study materials to come up with these kinds of spells."

menu de_choice2:
    de "How exactly would he get a hold of that?"

    "He stole it from the school's dark magic archives.":
        jump de_choice2_a

    "He was given it from someone with clearance.":
        jump de_choice2_b

    "He happened to find it from an Occult shop.":
        jump de_choice2_c

label de_choice2_a:
    de "As adept as he seems to be at magic, it's possible he simply duped the school's security team."
    de "The systems in place are pretty good at preventing physical theft."
    de "He most likely tricked one of the professors into giving him access."

    $ kt_villain = kt_villain + 1
    jump end_ingredients2


label de_choice2_b:
    de "I find it hard to believe that he could have infiltrated the school's archives."
    de "Modern golem security systems have made that much more difficult than it was in the past."
    de "I'm not sure why, but it's possible someone who had access themselves could have given it to him."

    $ kt_hero = kt_hero + 1
    jump end_ingredients2

label de_choice2_c:
    de "I've heard more and more stories about Occult shops popping up with strange and often illegal offerings."
    de "If Kellum got mixed up with these places, then he might have bought more than he bargained for."

    $ kt_victim = kt_victim + 1
    jump end_ingredients2

label end_ingredients2:
    de "Either way it puts those ingredients into context."
    de "It's no simple potion he was working on, nothing in this book would be as benign as that."
    de "Here we go, page 478."
    de "Ingredients required: Dogwart, Snail Urine, Griffin's tongue...and a bunch of other stuff he would be able to find."
    de "The problem I'm having is that this doesn't exactly look explosive in nature, at least not like we've seen around the school."
    de "Could he be working on something else? Something even worse?"

    jump actTwoOutro

label actTwoOutro:
    #"DEBUG: End of Act Two"
    jump return_actTwo