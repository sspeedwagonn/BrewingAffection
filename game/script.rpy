#TODO
# DO THIS
# BEFORE
# SUBMITTING!!!!!!!
# ADD COFFEE MAKING MECHANICS
# MAKE THE NOISE OF THE ESPRESSO MACHINE MORE RELEVANT
# ADD CHARACTER ART

define phone = Character("Phone")
define mom = Character("Mom")
define s = Character("Sister") #she needs a name
define jj = Character("Java Joe")
define em = Character("Espresso Machine")
define mw = Character("Matt White") #quirky business man, corporate guy. he's pretty sweet
define cb = Character("Cole Blue") # cold and distant at first, but grows to be pretty cool! maybe he's been hurt by a barista once and doesn't want to repeat "the incident"
define bv = Character("Brae Vae") #the artist, likes to use the cafe to work on her art n stuff
define ac = Character("Anthony Cino") #rich guy who thinks he's a gift to this world. he's kind of quirky but not in a great way. doesn't want to be with MC if the MC doesnt make bank
define unknown = Character("???")
define ct = Character("Customer Tutorialman")

default fired = 0
default matt = 0
default cole = 0
default brae = 0
default anthony = 0
default java = 0
default tips = 0
default sister = 0
# The game starts here.

label start:
    #Empty room
    show room

    "Oh no, I'm almost late for work!"

    #MC appears in front of a mirror
    show mc

    "Looking good... wait, I'm missing something!"

    "My name tag! Oh gosh, the name must have rubbed off... let me write it again."

    $ mc = renpy.input("Write your name!", length=32)

    $ mc = mc.strip()
    if not mc:
        $ mc="Brewce"

    mc "And then pronouns..." #idk if i need this no one really refers to the MC ever

    menu:
        "What are your pronouns?"
        "They/them":
            ## This is how you will set the player's pronouns. This string
            ## should match the ones you wrote in possible_pronouns.
            $ pronoun = "they/them"
        "She/her":
            $ pronoun = "she/her"
        "He/him":
            $ pronoun = "he/him"
    mc "Alright, let's get to work!"

    phone "Buzz, buzz... New text from Mom!"

    mc "What does she want now?"

    mom "[mc], are you still coming to your sister's wedding?"

    mom "She wanted to know."

    mc "She could've just text me directly..."

    mom "She thinks you hate her after she didn't include you in the wedding party."

    mom "Anyways! Make sure to bring a date! That is your sister's one request"

    mc "What?"

    mc "Why does she care?"

    mom "She just wants you to have a good time."

    mc "Why do I need a date to have a good time?"

    mom "Don't make this so difficult... just bring a date. It'll make your sister happy!"

    mc "Fine..."

    mc "I guess that means I need to find someone to go with. But I need to get to work! I'm already late."

    hide room
    show cafe
    show mc at right
    # MC makes it to the coffee shop
    show jj at left
    with move
    jj "[mc]! Where have you been? You're 7 meownites and 46 seconds late."

    menu where_been:
        "I don't have to explain myself to you, Java Joe.":
            jj "What's with the cattitude?"

        "My mom was texting me. She wants me to find a date.":
            jj "You've got to be kitten me."

    jj "Well, anyways, we need you back here. The morning rush is about to come and-"

    em "BBBRRRRRRRRRRRRRRRRRRRRRR"

    jj "And there's no time to paws."

    mc "What's with that noise?"

    jj "It's just the mew espresso machine."

    mc "Are you sure it's \"mew\"...?"

    jj "It is mew, it's just like that for now. The packaging said after some uses it won't be that loud anymore."

    jj "Worry about the customers, not the sound. If you don't hear a customer, just ask them to repeat themselves."

    mc "Alright..."

    hide jj
    show mc at center with move

    mc "Maybe I can find a customer who wants to be my date to the wedding!"

    # SHIFT 1: START -- add some sort of title card
    # Bad ending available: getting fired for messing up orders

    mc "I can help the next customer!"

    show ct at left
    show mc at right with move
    unknown "Hi, can I ask you something?"

    mc "Sure..."

    ct "My name is Customer Tutorialman. Do you know how to make coffee?"

    menu tutorial_q:
        "No, I could use a tutorial. If you happen to do those sort of things...":
            jump tutorial

        "Of course I know how to make coffee. Can I get something started for you?":
            ct "No, thanks. I didn't really want a coffee."
            mc "Uh, alright then. Huh."
            jump shift_one

# SHIFT ONE: get to know the potential love interests
    label shift_one:
        hide ct
        mc "Let's get this shift started!"

        #Introduction to matt white, if the
        show mw
        mw "Hi, one flat white, please! For Matt White."

        menu mw_int_1:
            "Sure, I'll get that started for you!": #nuetral -- not sure if i spelt that correctly. neutral?
                mw "Great, thanks!" # no change, go to making coffee
                $ java += 1 # java joe personally likes it when MC sells coffee and gets to it!
                $ matt += 1 #he's just really happy for the kindness and help. he usually makes coffee at home or at the office - this is a little treat for him
                $ fired += 1 # so player has a chance to be rude if they want to later on
                jump mw_coffee_1

            "Sure! I love your tie, by the way!": #pos
                mw "Oh, thank you. I got it from my father, Matt White Sr!" #go to an extended interaction, then coffee
                $ matt += 2 # matt doesn't get a lot of compliments, so this means a lot to him
                $ fired += 2
                jump mw_ext_1

            "A flat white? For Matt White? Are you kidding me... no!": #neg and fired++
                mw "Uh... okay."
                hide mw
                mc "Next!"
                $ fired -= 1
                $ matt -= 3
                jump bv_int_1

        label mw_ext_1: #matt points! get your matt points here! he's probably the absolute easiest to romance
            menu mw_question_1:
                "So, do you always get a flat white?":
                    $ matt += 2
                    mw "Of course! It's the best."
                    mc "What do you like most about it?"
                    mw "The texture. Is that a weird thing to say?"
                    menu weird_thing:
                        "I don't think that's weird at all.":
                            mw "That's good to hear. Can I say something else weird?"
                            $ matt += 2
                            menu weird_thing_ext:
                                "Sure, go for it!":
                                    mw "Well..."
                                    mw "I'm glad I came here. You're really nice!"
                                    mc "That's so sweet! Thank you!"
                                    mw "I'll have to come again after this. Unfortunately, I have a meeting soon, so I can't stick around!"
                                    mc "Well, let me get you that flat white, then!"
                                    $ matt += 3
                                    jump mw_coffee_1

                                "I'd rather just make your coffee.":
                                    mw "Oh, yeah, of course!"
                                    jump mw_coffee_1

                        "I would think you prefer the strong coffee flavor.":
                            mw "I don't actually like coffee that much."
                            mc "Really? Why not go for something else?"
                            mw "Something just draws me to the flat whites. I'm not sure what, though."
                            $ matt += 1
                            mc "Well, let me get it started for you then!"
                            jump mw_coffee_1

                        "You drink coffee... for the texture?":
                            mw "That was a weird thing to say, then, huh?"
                            mc "..."
                            mc "...I'll get that coffee started"
                            $ matt -= 1
                            jump mw_coffee_1

                "Are you a businessman?":
                    mw "Haha, businessman is way too formal. I'm just an accountant."
                    mc "So you like numbers?"
                    mw "Mostly the numbers on my paycheck. Other than that, it's a job." #white boy swag moment

                "What's your dad like?": #weird f'in question lmao
                    mw "Oh, he's uh... dead. Hit by a car."
                    mc "Oh... I'm sorry to hear."
                    $matt -= 1
                    menu recover_matt:
                        "Should I try to recover this..."

                        "Yes.":
                            mc "I can comp your coffee... I'm really sorry."
                            mw "Don't worry about it!"
                            $ matt += 1

                        "No.":
                            mc "What kind of car?"
                            mw "It was a BMW... can I just get my coffee please?"
                            $ matt -= 3 #he's strange, but that doesn't mean you can just say whatever and get away with it
                            # he deadass probably won't come back after this

        label mw_coffee_1:
            #coffee making here
            mc "Here's your coffee"
            mw "Wow, that's great!"
            if matt <= 3:
                $tip += 5
            if matt <= 1: #he's the type of guy to always tip no matter what, but he'll tip extra if he likes MC
                $ tip += 2
            else:
                $ tip += 1
                jump bv_int_1

        label bv_int_1:
            mc "Next!"
            show brae
            mc "Hi, what can I make for you?"
            bv "Hey, what's the wifi password?"
            menu bv_int_1_ext:
                "You don't want a coffee?":
                    bv "Oh, I already got one when I came here."
                    mc "How long have you been here for?"
                    bv "As soon as Java Joe unlocked the doors! The cafe is the best place for work, you know!"
                    menu bv_work:
                        "What kind of work?":
                        "":

        label fired_warning:
            if fired = -1: #first and only warning, add this check better later on.
                jj "[mc]! That's not how we treat customers. Don't furget, this is an at-will employement state."
                jj "I will fire you if you can't act like a purrfessional!"
        # End of shift
        # If fired = 3, player gets fired and game ends
        if fired <= -3:
            jump bad_ending_fired

        menu talk_sister_1:
            "Should I text my sister...?"

            "I should.":
                mc "Maybe she'd appreciate hearing about my plan since she wants me to bring a date so bad!"
                jump text_sister_1

            "No, I won't.":
                mc "She's probably too busy prepping for her wedding."
                mc "I need to get to bed, anyways..."
                $ sister -= 1 #maybe mc should talk to their sister... :(
                jump shift_2

        label text_sister_1:
        #there'll be left over texts of attempted communication, kind of one sided
            mc "Hey!"
            mc "I'm excited for your wedding!!! How's everything been going?"
            $sister += 1 #she appreciates the effort but relationships arent repaired in a text
            s "..." #typing
            s "👍"

# SHIFT TWO: Get to know them better, one LI drops off
    label shift_two:

# SHIFT THREE: Ones who the MC shows interest in start to appear frequently, divulge more
    label shift_three:
# SHIFT FOUR: Based on pursued LI
    label shift_four:
# SHIFT FIVE: The confession, based on pursued LI
    label shift_five:
# ENDINGS
    return

label tutorial:
    ct "Let's start with taking orders."
    jump shift_one

label bad_ending_fired:
    jj "[mc], we talked about this, and frankly, I'm so disappointed I can't even make a cat pun."
    mc "But-"
    jj "I'm sorry about whatever you're going through, but you didn't need to bring it to work..."
    jj "You're fired."

    #later, dialogue needs heeeeaaaavvvvvyyyyy refining
    mc "I need to tell my mom I got fired..."
    mc "Mom, I got fired."
    mom "What? You were supposed to find a date!"
    mc "It's not about a date anymore."
    mom "Don't bother showing up to your sister's wedding..."
    return