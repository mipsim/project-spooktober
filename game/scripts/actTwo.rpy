label actTwo:
    # Setup ---------------------------
    scene bg temp2
    with dissolve

    show detective_temp
    with easeinleft

    play music "audio/LaytonTheme.mp3"
    # ---------------------------------

    "DEBUG: Intro"
    de "So this is the room in question..."
    de "Smells like wet dog, but otherwise it seems about par for the course."
    de "In fact, it's rather tidy given the current state of the university."
    de "Let's start by taking a look around"

menu choose_item:
    de "What should I look at?"

    "Bookshelf" if itemBookshelf_checked != True:
        jump item_bookshelf

    "Spilled ink" if itemInk_checked != True:
        jump item_ink

    "Ingredients on table" if itemIngredients_checked != True:
        if itemInk_checked == True:
            jump item_ingredients2
        else:
            jump item_ingredients1

label item_bookshelf:
    "DEBUG: Bookshelf"
    de "Let's see, anything interesting?"
    de "'Legal histroy of transmogrification' nope, 'Counter Inductive Spell structures for Undergrads', no thanks, 'Notes on the use of spark spells in general combat' yeah I'll pass."
    de "Hmmm... this one seems interesting, 'Caster in the rye'"
    de "It was required reading at my magic school, but I can't imagine it's part of any modern curriculum."
    de "Not that it means anything on its own, but let's just hope he doesn't identify with the main character too much."
    de "Ah, here's something interesting!"
    de "'Skill improvement 7th edition' These books are supposed to be banned from university."
    de "They use enchanted ink to automatically make you a better magician"
    de "Useful for improving worker productivity, but it doesn't actually transfer any knowledge of how the magic works."
    de "It's strange the Kellum would have anything to do with it, usually students using books like this get found out when someone asks them a slightly too intelligent question."

    $ itemBookshelf_checked = True
    jump choose_item

label item_ink:    
    "DEBUG: Spilled Ink"
    de "Spilled ink on the table, a classic question of causality."
    de "Of all the thousands of possible actions, not to mention the addition of spells, incantations, imbibements, enchantments and all the rest."
    de "Out of all of those I have to narrow it down to a single..."
    "-- Display Pawprint"
    de "Oh, it seems he has a dog."
    de "Well, that was quite the simple mystery."
    de "It seems this ferocious beast has left a trail all the way back to its den: the lower cubby of the autobiography section."
    "-- Opens cubby"
    "-- Dog growls"
    de "Well met familiar, may I ask what you're sitting on?"
    "-- Dog growls again"
    de "I see, well I won't make any headway just asking it nicely."
    "-- Shows can of empty dog food 'Curio Brand Dog Food'"
    de "Well, maybe if I can find a can that isn't empty he'll open up to me."

    $ itemInk_checked = True
    jump choose_item

label item_ingredients1:
    "DEBUG: Ingredients"
    "-- looks at a bunch of innocuous seeming ingredients on the table"
    "-- notices a tin of dog food"
    de "Ingredients it seems, and not the kind you cook with."
    de "Well, I supposed you could cook with this one."
    "-- shows dog food 'Cerberus Chum'"
    de "But the rest are 'medicinal' at best."
    de "Let's see here, dogwart, milliweed, griffin's tongue, and snail urine."
    de "All mainstays in the wizarding pharmaceutical industry, but not exactly household names."
    de "Not that they are hard to get your hands on, they can all be extracted from stuff you can get over the counter at any wizard clinic worth its summoning salt."

    jump choose_item

label item_ingredients2:
    "DEBUG: Ingredients after Spilled Ink"
    "-- takes food to dog, dog gives up book"
    "-- after reading the book you realize that the ingredients are for a nefarious purpose"
    "-- you wonder how he got a hold of such a dangerous book, only academics with unrestricted access can get hold of books like this"
    de "Well I bet I can get that dog to hand over the book he’s protecting with a little state sponsored bribery."
    "-- Fills bowl with food"
    de "Here Filbo, don’t you want some food?"
    "-- Dog growls"
    de "Well I guess he has a pretty strong preference for 'Curio Brand'"
    de "Let's see what we can do for the spoiled mutt."
    "-- Closes the Cubby"
    de "Just a quick little swap...and we are good to go."
    "-- Gathers the dog food from the bowl into a can of 'Curio Brand Dog Food'"
    "-- Opens the Cubby"
    de "Alright, I got you the good stuff this time, you like Curio Don't you?"
    de "Look I got a fresh new can of it for you"
    "-- Dog is excited"
    "-- Pours the food into a bowl and pushes it over to the dog."
    "-- Dog eats it excitedly"
    de "Perfect, and if you don't mind I'm going to borrow this dog bed from you."
    de "Doesn't look particularly comfortable anyhow."
    "-- Show book cover"
    de "Well I'll be, We found the smoking gun didn't we Toto?"
    de "Dark Arts, Summoning Demons, Transforming Flesh, etc. etc."
    de "Not the kind of stuff you get into freshman year."
    de "In fact I would be surprised that any student could get ther hands on this without outright stealing it, and I find that hard to believe with the new advancements in golem security systems."
    de "Perhaps he got it on loan from someone he trusts?"
    de "Either way it puts those ingredients into context."
    de "It's no simple potion he was working on, nothing in this book would be as benign as that."
    de "Here we go, page 478, Ingredients required: Dogwart, Snail Urine, Griffin's tongue...and a bunch of other stuff he would be able to find."
    de "The problem I'm having is that this doesn't exactly look explosive in nature, at least not like we've seen around the school."
    de "Could he be working on something else? Something even worse?"

    $ itemIngredients_checked = True
    jump actTwoOutro

label actTwoOutro:
    "DEBUG: Outro"
    jump return_actTwo