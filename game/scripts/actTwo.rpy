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
    de "'Legal history of transmogrification.'"
    de "Nope."
    de "'Counter Inductive Spell structures for Undergrads.'"
    de "No thanks."
    de "'Notes on the use of spark spells in general combat.'"
    de "Yeah I'll pass."
    de "Hmmm...this one seems interesting."
    de "'Caster in the rye.'"
    de "It was required reading at my magic school, but I can't imagine it's part of any modern curriculum."
    de "Not that it means anything on its own, but let's just hope he doesn't identify with the main character too much."
    de "Ah, here's something interesting!"
    de "'Skill improvement 7th edition.'"
    de "These books are supposed to be banned from university."
    de "They use enchanted ink to automatically make you a better magician."
    de "Useful for improving worker productivity, but it doesn't actually transfer any knowledge of how the magic works."
    de "It's strange the Kellum would have anything to do with it."
    de "Usually students using books like this get found out when someone asks them a slightly too intelligent question."

    $ itemBookshelf_checked = True
    jump choose_item

label item_ink:    
    de "Spilled ink on the table, a classic question of causality."
    de "Of all the thousands of possible actions, not to mention the addition of spells, incantations, imbibements, enchantments and all the rest."
    de "Out of all of those I have to narrow it down to a single..."
    
    #"-- Display Pawprint"    
    show de_base_dark with dissolve
    show prop_pawprints at truecenter with easeintop

    de "Oh, it seems he has a dog."

    hide prop_pawprints with easeoutbottom
    hide de_base_dark with dissolve

    de "Well, that was quite the simple mystery."
    de "It seems this ferocious beast has left a trail all the way back to its den: the lower cubby of the autobiography section."
    "-- Opens cubby"
    "-- Dog growls"
    de "Well met familiar, may I ask what you're sitting on?"
    "-- Dog growls again"
    de "I see, well I won't make any headway just asking it nicely."
    
    #"-- Shows cans of empty dog food 'Curio Brand Dog Food.'"
    show de_base_dark with dissolve
    show prop_canempty at truecenter with easeintop
    
    de "Well, maybe if I can find a can that isn't empty he'll open up to me."

    hide prop_canempty with easeoutbottom
    hide de_base_dark with dissolve

    $ itemInk_checked = True
    jump choose_item

label item_ingredients1:
    show de_base_dark with dissolve
    show prop_ingredients at truecenter with easeintop

    de "Ingredients it seems, and not the kind you cook with."
    
    hide prop_ingredients with easeoutbottom
    show prop_canfull at truecenter with easeintop

    de "Well, I supposed you could cook with this one."

    hide prop_canfull with easeoutbottom
    hide de_base_dark with dissolve

    #"-- Shows dog food 'Cerberus Chum'"

    de "But the rest are 'medicinal' at best."
    de "Let's see here, dogwart, milliweed, griffin's tongue, and snail urine."
    de "All mainstays in the wizarding pharmaceutical industry, but not exactly household names."
    de "Not that they are hard to get your hands on."
    de "They can all be extracted from stuff you can get over the counter at any wizard clinic worth its summoning salt."

    $ itemIngredients_checked = True

    if itemInk_checked == True:
        jump item_ingredients2
    else:
        jump choose_item

label item_ingredients2:
    de "Well I bet I can get that dog to hand over the book he’s protecting with a little state sponsored bribery."
    
    #"-- Fills bowl with food"
    show de_base_dark with dissolve
    show prop_bowl at truecenter with easeintop

    de "Here buddy, don’t you want some food?"
    hide prop_bowl with easeoutbottom
    hide de_base_dark with dissolve

    "-- Dog growls"
    de "Well I guess he has a pretty strong preference for 'Curio Brand'"
    de "Let's see what we can do for the spoiled mutt."
    "-- Closes the Cubby"
    de "Just a quick little swap...and we are good to go."
    
    #"-- Gathers the dog food from the bowl into a can of 'Curio Brand Dog Food'"
    show de_base_dark with dissolve
    show prop_canfull at truecenter with easeintop

    "-- Opens the Cubby"
    de "Alright, I got you the good stuff this time."
    hide prop_canfull with easeoutbottom
    hide de_base_dark with dissolve

    de "You like Curio don't you?"
    de "Look I got a fresh new can of it for you"
    "-- Dog is excited"
    "-- Pours the food into a bowl and pushes it over to the dog"
    "-- Dog eats it excitedly"
    de "Perfect, and if you don't mind I'm going to borrow this dog bed from you."
    de "Doesn't look particularly comfortable anyhow."
    
    #"-- Show book cover"
    show de_base_dark with dissolve
    show prop_tome at truecenter with easeintop

    de "Well I'll be, We found the smoking gun didn't we Toto?"
    hide prop_tome with easeoutbottom
    hide de_base_dark with dissolve

    de "Dark Arts, Summoning Demons, Transforming Flesh, etc. etc."
    de "Not the kind of stuff you get into freshman year."
    de "These are some real 'I knew them before they were cool' type spells."
    de "In fact I would be surprised that any student could get ther hands on this without outright stealing it."
    de "I find that hard to believe with the new advancements in golem security systems."
    de "Perhaps he got it on loan from someone he trusts?"
    de "Either way it puts those ingredients into context."
    de "It's no simple potion he was working on, nothing in this book would be as benign as that."
    de "Here we go, page 478."
    de "Ingredients required: Dogwart, Snail Urine, Griffin's tongue...and a bunch of other stuff he would be able to find."
    de "The problem I'm having is that this doesn't exactly look explosive in nature, at least not like we've seen around the school."
    de "Could he be working on something else? Something even worse?"

    jump actTwoOutro

label actTwoOutro:
    "DEBUG: Outro"
    jump return_actTwo