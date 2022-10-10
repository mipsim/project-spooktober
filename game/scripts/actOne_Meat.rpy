label Meethed:
    # Setup ---------------------------
    scene bg2a with dissolve

    show me_sad with easeinleft
    # ---------------------------------
    mc "Excuse me. Mind if I...oh by the stars..."
    me "‘Lo...Prof..."
    mc "Erm. Okay. Hello to you too. So can you tell me your name?"
    
    hide me_sad
    show me_base
    
    me "You...no...reco...me?"
    mc "Pardon?"
    me "You...no...reco...me...."
    mc "Reco...No. My apologies. I do not recognize you."
    me "No...blem..."
    me "Nem...eye...sec..."
    mc "Erm...nem..."

    hide me_base
    show me_angry

    me "EYE...SEC..." with vpunch
    mc "Eye...Issac?"

    hide me_angry
    show me_base
    
    me "Yeh..."

    mc "Alright. Issac. Got it. Now, I would like to ask you some questions, but...erm...how should we go about this?"
    me "Me...want...ask...you..."
    me "Can...under...stan...clear..."
    mc "So you can understand everything I’m saying. Every word."
    me "A...firm..."
    mc "I see. Could it be that your body is causing you to struggle to speak?"
    me "Core...ect..."

    mc "Ah. My apologies, then."

menu meat_choice1:
    mc "Ah. My apologies, then."

    "Can you tell me what happened here?":
        jump meat_choice1a

    "How did this happen to you?":
        jump meat_choice1b

    "Where is Kellum?":
        jump meat_choice1c

label meat_choice1a:
    me "Not...much..."
    me "Boom...red...light...Then...pain...body...morph...this..."

    hide me_base
    show me_sad

    me "That...all..."
    mc "I see...That must have been pretty sudden."

    $ meat_1a_checked = True

    hide me_sad
    show me_base

    jump meat_choice2

label meat_choice1b:
    
    hide me_sad
    show me_base

    me "Cattle...in...body...likely..."
    mc "Cattle? So you’ve been eating an excess amount of beef?"

    hide me_sad
    show me_base
    me "No...Cattle...liss..."
    mc "Cattle-liss...You mean a catayst?"
    me "Yeh."
    mc "How did you get it?"

    hide me_base
    show me_angry

    me "Kellum..."
    mc "Kellum gave it to you?"
    me "Dirty...trick..."
    mc "Can you elaborate?"
    me "Kellum...always...best..."

    hide me_angry
    show me_sad

    me "All...I...get...grades...work...effort...not matter..."
    
    hide me_sad
    show me_angry

    me "Kellum...always...shadow...All...cause...Kellum...good...look..."
    mc "So you were jealous of Kellum, because he always overshadowed you through his good looks?"
    
    hide me_angry
    show me_sad

    me "Will...admit...envy..."

    hide me_sad
    show me_base

    me "But...one day...Kellum...give...cattle...Said...will...make me...as...good...look...as him..."
    mc "Kellum offered you the catalyst, saying it would make you as good looking as he is."
    me "First...skeptic...but...decide...to humor..."
    me "Small effect...at...first...but...after...light...turn to...this..."
    mc "You were initially skeptical, but decided to humor him."
    mc "The catalyst had small effects at first, but after the incident you turned into what you are now..."
    mc "Is that right?"

    hide me_base
    show me_sad

    me "Yeh..."
    me "Sick...joke...No...forgive..."
    mc "I’m...sorry to hear that."

    $ meat_1b_checked = True

    hide me_sad
    show me_base

    jump meat_choice2

label meat_choice1c:
    me "Don’t know...No...see...him...when...wake..."
    mc "I see."
    me "My...advice...stay...away..."
    mc "You don’t want me to pursue Kellum? Why is that?"
    me "Saw...him...with you...often...Must...want...favor..."

    hide me_base
    show me_angry

    me "No...fall...for...lie..."
    mc "I will proceed with caution then."

    $ meat_1c_checked = True

    hide me_sad
    show me_base

    jump meat_choice2

menu meat_choice2:
    mc "What else should I ask Issac?"

    "Can you tell me what happened here?" if meat_1a_checked == False:
        jump meat_choice1a

    "How did this happen to you?" if meat_1b_checked == False:
        jump meat_choice1b

    "Where is Kellum?" if meat_1c_checked == False:
        jump meat_choice1c

label end_meat:
    mc "I think that’s all the questions I have for you at the moment."
    me "Take...care..."

    $ me_checked = True
    jump returnFromStudent