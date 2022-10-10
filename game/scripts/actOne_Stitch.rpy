label Stelivia:
    # Setup ---------------------------
    scene bg2a with dissolve

    show st_sad with easeinleft
    # ---------------------------------

    st "No no no...it can’t-this wasn’t how this was supposed to go."

    hide st_sad
    show st_look

    st "{i}As much as I’d like to agree, denying the situation does not help in the slightest.{/i}"

    hide st_look
    show st_sad

    st "Then what am I suppos-?!"
    mc "Um. Hello?"

    hide st_sad
    show st_base

    st "Ah! Professor!"
    mc "Ah! My apologies. I-er didn’t mean to startle you...erm..."
    mc "Sorry. Who are you...two?"

    hide st_base
    show st_sad

    st "Who am-? How do you not know my name? It’s several months into the term."

    hide st_sad
    show st_look

    st "{i}Then again, in all fairness, I doubt I’d be recognizable in this state.{/i}"
    st "Hm. I guess that’s true."

    hide st_look
    show st_base

    st "{i}You may have known me-...I mean us- as Stephanie Papillon and Olivia Mendritch.{/i}"
    st "{i}But for the time being you can refer to me as...Stelivia, I suppose.{/i}"

    hide st_base
    show st_look

    st "Stelivia? Really?"
    st "{i}I’m not good at thinking on the spot. Alright? Do you have any better suggestions?{/i}"
    st "Fine. I’ll bite."
    mc "Alright, Ms. Stitch. Can you tell me what happened?"

    hide st_look
    show st_base

    st "{i}To be honest I don’t know.{/i}"
    st "{i}I’m still in the middle of processing everything that happened, so I can’t offer more than a general description.{/i}"
    mc "Even a general description will suffice."
    mc "You don’t need to be so formal with me. I’d rather you be as comfortable as possible."
    st "Oh. Okay."

    st "Well, all that I know happened was that it was a pretty normal day until, BOOM, there was a sudden flash of red light."

    hide st_base
    show st_sad

    st "The next thing I knew, I turned into this."
    st "I don’t know any more than that."
    mc "Do you know how this happened?"

    hide st_sad
    show st_base

    st "That’s exactly what I’ve been trying to figure out!"
    st "You think I have any ideas here?"

    hide st_base
    show st_look

    st "{i}That said, I can make an educated guess.{/i}"

    hide st_look
    show st_base

    mc "Feel free to share it."
    st "{i}I think it may have something to do with this catalyst on my body.{/i}"
    mc "Catalyst? You mean this gem?"
    st "{i}Yes.{/i}"
    mc "How did you get it?"

    hide st_base
    show st_look

    st "That...is a long story."
    mc "Take your time."

    hide st_look
    show st_base

    st "{i}Okay. So...the short of it is...{/i}"
    st "...Kellum gave it to me."
    mc "He gave it to you? As a gift?"

    st "I think so?"

    hide st_base
    show st_look

    st "{i}It was more like...we asked him for it.{/i}"
    st "{i}We approached him one day asking for advice on how he can fit in with different social environments.{/i}"

    hide st_look
    show st_sad

    st "{i}When I...I mean *we* were separate, we fit in well with our own social niches, but struggled to fit in anywhere else.{/i}"

    hide st_sad
    show st_base

    st "Stephanie was a social butterfly with many friends, but struggled to discuss academic subjects with anyone."

    hide st_base
    show st_look

    st "{i}Olivia, on the other hand, could hold her own in academic presentations and discussions, but could never function in a casual conversation.{/i}"

    hide st_look
    show st_base

    st "Kellum seemed to thrive in any conversation, academic or casual. So we asked him for some advice."
    st "{i}In response, he gave us both this catalyst, promising that it will give us the other’s best qualities.{/i}"
    st "{i}It would be as if...we were the same person.{/i}"

    mc "I see. What about the other students? Have you perhaps come across Kellum?"

    hide st_base
    show st_sad

    st "{i}No I haven’t seen him after the incident.{/i}"
    mc "Where do you think he is now?"

    hide st_sad
    show st_base

    st "If anyone among us had any idea, it would be you."
    st "More often than not I would see him hanging with you. Chatting it up like...good ol’ chums."
    st "He just seemed more comfortable around you."
    mc "I see..."

    mc "I think that’s all the questions I have for you at the moment."
    st "{i}Oh. Well when you see Kellum, give him my regards.{/i}"

    hide st_base
    show st_look

    st "Given how he’s looked lately, I think he could use some."
    mc "I will. Goodbye, Stelivia."

    $ st_checked = True
    jump returnFromStudent