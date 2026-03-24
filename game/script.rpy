# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define phone = Character("Phone")
define mom = Character("Mom")
define jj = Character("Java Joe")
define em = Character("Espresso Machine")
define mw = Character("Matt White")
define ar = Character("Amir Ricano")
define cb = Character("Cole Blue")
define bv = Character("Brae Vae")
define ac = Character("Anthony Cino")
define unknown = Character("???")
define ct = Character("Customer Tutorialman")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    "Oh no, I'm almost late for work!"

    "My name tag! Oh gosh, the name rubbed off... let me write it again."

    $ mc = renpy.input("Write your name!", length=32)

    $ mc = mc.strip()
    if not mc:
        $ mc="Brewce"

    mc "And then pronouns..."

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

    # MC makes it to the coffee shop, it's time themed
    show jj
    jj "[mc]! Where have you been? You're 7 minutes and 46 seconds late."

    menu where_been:
        "..."
        "I don't have to explain myself to you, Java Joe.":
            jj "What's with the cattitude?"

        "My mom was texting me. She wants me to find a date.":
            jj "You've got to be kitten me."

    jj "Well, anyways, we need you back here. The morning rush is about to come and-"

    em "BBBRRRRRRRRRRRRRRRRRRRRRR"

    jj "And there's no time to paws."

    mc "What's with that noise?"

    jj "It's just the new espresso machine."

    mc "Are you sure it's new...?"

    jj "It is new, it's just like that for now. The packaging said after some uses it won't be that loud anymore."

    jj "Worry about the customers, not the sound. If you don't hear a customer, just ask them to repeat themselves."

    mc "Alright..."

    hide jj

    mc "Maybe I can find a customer to be my date to the wedding!"

    # SHIFT 1: START -- add some sort of title card
    # Bad ending: getting fired for messing up orders

    mc "I can help the next customer!"

    show ct
    unknown "Hi, can I ask you something?"

    mc "Sure..."

    ct "My name is Customer Tutorialman. Do you know what you're doing?"

    menu tutorial_q:
        "No, I could use a tutorial.":
            jump tutorial

        "Of course I do.":
            ct "Well, suit yourself! That's all. I didn't really want a coffee."
            jump shift_one

    label shift_one:
        hide ct
        mc "Let's get this shift started!"

        show mw
        mw "Hi, one flat white, please!"

        menu mw_int_1:
            "Sure, I'll get that started for you!":
                jump mw_coffee_1

            ""

    return

label tutorial:
    ct "Let's start with taking orders."
    jump shift_one
