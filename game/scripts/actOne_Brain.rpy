label Hilde:
    # Setup ---------------------------
    scene bg2a with dissolve

    show hi_base with easeinleft

    $ hilde_name = "???"
    # ---------------------------------

    mc "Hello, mind if I ask a few questions?"

    hide hi_bored
    show hi_uhh

    hi "Um...professor? Everything alright?"
    mc "You'll have to forgive me, the explosion gave me some kind of amnesia."
    mc "So if I knew you, I forgot."
    mc "I hope you'll forgive me."

    hide hi_uhh
    show hi_base

    hi "Ok then, ask away."

menu hilde_1:
    hi "Ok then, ask away."

    "What's your name?":
        jump hilde_1a

    "Before the event, did you notice anything strange at the academy?":
        jump hilde_1b

    "Do you know anything about what happened?":
        jump hilde_1c

label hilde_1a:
    $ hilde_name = "Hilde"

    hide hi_base
    show hi_uhh

    hi "Hilde, do you really not remember me?"

    hide hi_uhh
    show hi_bored

    hi "Sat in the back of your class..."
    hi "Really good student..."

    hide hi_bored
    show hi_happy

    hi "He he..."
    mc "No, like I said I have amnesia."

    hide hi_happy
    show hi_base

    hi "Yeah, but it can't have wiped all of your memories."
    hi "There's like 27 different types of amnesia."

    hide hi_base
    show hi_uhh

    hi "Retrograde amnesia, traumatic amnesia, psychogenic amnesia, elemental amnesia, revival amnesia-"
    mc "Okay, I get it. You know a thing or two."
    mc "Maybe I knew what some of those meant before, but right now I do not."
    mc "And I don't think terminology is going to suddenly unlock my memory palace."

    hide hi_uhh
    show hi_base

    hi "I guess not, figured you might want to know anyways."

menu hilde_1aa:
    hi "I guess not, figured you might want to know anyways."

    "Ok, fine. Let's hear your theories about my amnesia.":
        jump hilde_1ab

label hilde_1ab:

    hide hi_base
    show hi_happy

    hi "Perfect!"

    hide hi_happy
    show hi_base

    hi "The current magical consensus on amnesia is pretty divided."
    hi "But given that we have a good idea of the source of the trauma we might be able to figure out how it works."
    
    hide hi_happy
    show hi_uhh

    hi "Can you remember anything about your childhood?"
    mc "Yes, of course I can."

    hide hi_uhh
    show hi_happy

    hi "That takes it down to 16 possibilities."

    hide hi_happy
    show hi_uhh

    hi "And your memory post accident seems fine?"
    mc "As far as I can tell."
    hi "Then you probably have...let's see..."
    hi "Hmmm..."

    hide hi hi_uhh
    show hi_base

    hi "You know it's harder than I thought to figure this out."
    hi "I would probably have to focus and draw out the information."

    hide hi_base
    show hi_bored

    hi "Sorry for the sudden change, but I have a headache."
    hi "I just can't be bothered."
    mc "That's alright."
    hi "It's important I know...I just..."
    mc "Really, it's fine. Let's move on."

    $ hilde_1a_checked = True
    $ num_hilde_checked = num_hilde_checked - 1

    hide hi_bored
    show hi_base

    jump hilde_2

label hilde_1b:

    hi "No, I've been kind of busy with my studies and all."
    mc "I see, you must have been one of my straight A students then."

    hide hi_base
    show hi_bored

    hi "Um...well..."
    hi "...Yeah, let's go with that."

menu hilde_1ba:
    hi "...Yeah, let's go with that."

    "Something wrong?":
        jump hilde_1bb

label hilde_1bb:

    hide hi_bored
    show hi_base

    hi "Ok, fine!"

    hide hi_base
    show hi_bored

    hi "I was failing your class. Is that what you wanted to hear?"
    mc "Um...I didn't mean it like that."

    hide hi_bored
    show hi_base

    hi "There is nothing more important to me than the expansion of humanity's knowledge, magical and scientific."
    hi "After we get wiped off this planet by atom bomb or by satan sumoning it's all we have to leave behind."

    hide hi_base
    show hi_bored

    hi "I know that..."
    hi "I know how important it is...I really do..."
    hi "But..."
    hi "I just can't do it."
    hi "There's nothing more demotivating and boring than the pursuit of knowledge."
    hi "And I couldn't even muster the bare minimum effort required to learn."
    hi "I tried to study, I really did."
    hi "But my eyes would glaze over."
    hi "The page would turn to a blur and I would forget a sentence I swear I just read."
    hi "How can it be that the thing I value most in the entire world..."
    hi "I'm utterly incapable of doing."
    mc "I...I'm sorry I couldn't help you."

    hide hi_bored
    show hi_base

    hi "Whatever, ask me something else."

    $ hilde_1b_checked = True
    $ num_hilde_checked = num_hilde_checked - 1
    jump hilde_2

label hilde_1c:
    hi "Yes, I do."
    mc "And..."
    
    hide hi_base
    show hi_uhh

    hi "I won't speak without my attorney present."
    mc "..."
    mc "You know this is a school right."
    mc "I might have amnesia, but I wasn't born yesterday."
    mc "Students don't have rights and you know it."

    hide hi_uhh
    show hi_bored

    hi "...Fine, where should I start?"

menu hilde_1ca:
    hi "...Fine, where should I start?"

    "What happened to your...um...head?":
        jump hilde_1cb

label hilde_1cb:
    hi "This one's my fault."

    hide hi_bored
    show hi_base

    hi "I was willing to do anything to get smarter."
    mc "And I guess studying just wasn't cutting it?"
    hi "Shut up!" with vpunch
    hi "Like you would understand."

    hide hi_base
    show hi_bored

    hi "You've probably always been able to study."
    hi "Don't look down on me like that."
    hi "Ugh...Sorry, this headache is killing me."

menu hilde_1cc:
    hi "Ugh...Sorry, this headache is killing me."

    "What happened to the school?":
        jump hilde_1cd

label hilde_1cd:

    hide hi_bored
    show hi_base

    hi "Some kind of explosion, not sure what caused it, but I was in my room at the time."
    mc "And what were you doing in your room?"

    hide hi_base
    show hi_uhh

    hi "I plead the-"
    mc "..."

    hide hi_uhh
    show hi_bored

    hi "Right, I already waived my rights."

    hide hi_bored
    show hi_base

    hi "This is probably going to get out anyways, so I'll be honest."
    hi "I was working on a potion, the results of which you can already see."
    hi "Not sure if the explosion messed with it while it was in progress."
    hi "But it didn't exactly go to plan."
    hi "As you have probably already ascertained."

menu hilde_1ce:
    hi "As you have probably already ascertained."

    "Do you know anything about me? I'm trying to figure out how I fit into all this.":
        jump hilde_1cf

label hilde_1cf:

    hide hi_base
    show hi_uhh

    hi "Well you're a professor at this academy, that much you already understand, yes?"
    mc "Yeah, the detective gave me a brief rundown."
    mc "And the clothes helped to convince me."
    mc "What kind of teacher was I?"

    hide hi_uhh
    show hi_base

    hi "Well I can't exactly give you an unbiased review, but I would say slightly above average."
    hi "I'm still not exactly satisfied with my education here."
    hi "But at least you seemed like you cared."

    $ hilde_1c_checked = True
    $ num_hilde_checked = num_hilde_checked - 1
    jump hilde_2

menu hilde_2:
    hi "Anything else? Or are we done here?"

    "What's your name?" if hilde_1a_checked == False:
        jump hilde_1a

    "Before the event, did you notice anything strange at the academy?" if hilde_1b_checked == False:
        jump hilde_1b

    "Do you know anything about what happened?" if hilde_1c_checked == False:
        jump hilde_1c

    "Any idea where Kellum went?" if num_hilde_checked <= 2 and hilde_2a_checked == False:
        jump hilde_2a

    "If there's anything I can do to help..." if num_hilde_checked == 0 and hilde_2b_checked == False:
        jump hilde_2b

label hilde_2a:

    hide hi_base
    show hi_uhh

    hi "No, I talked with him before this mess."
    hi "He seemed in a hurry, I think he was planning something big."

    hide hi_uhh
    show hi_bored

    hi "As for what it was or where it's happening I can't really help you, sorry."
    mc "No, it's alright. I've actually learned a lot from talking with you."
    mc "Thanks."

    $ hilde_2a_checked = True
    $ num_hilde_checked = num_hilde_checked - 1

    hide hi_bored
    show hi_base

    jump hilde_2

label hilde_2b:
    mc "You talked before about how important knowledge was to you."
    mc "I think it's important too, but it's nothing to beat yourself up about."
    mc "If there's anything I can do to help, or if you just want to talk about it..."

    hide hi_base
    show hi_bored

    hi "Really? Going to try to be my therapist?"
    hi "I have the combined sum of all publicly available academic knowledge on magic and psychology in my head."
    hi "What could you possibly say that I don't already know."
    mc "That I understand."

    hide hi_bored
    show hi_uhh

    hi "What? How could you understand?"
    hi "Not only do you have a job passing on knowledge. You also seem to genuinely enjoy your work."

    mc "I was like you too. I still am to some degree."
    mc "There are things that I thought were really important to me."
    mc "But I just couldn't find the motivation to do it."
    mc "I wanted to be a Hallowed Artificer when I was younger."
    mc "I trained hard for it, but even early on I knew I didn't have the chops for it."
    mc "In the end I settled for teaching."
    mc "Not just because it was important, but because I saw myself in that role."
    mc "It's not just about what you want to happen in the world."
    mc "You owe it to yourself to see where you fit in that picture too."

    hide hi_uhh
    show hi_base

    hi "..."

    hide hi_base
    show hi_happy

    hi "Thanks."
    
    $ hi_checked = True
    jump returnFromStudent