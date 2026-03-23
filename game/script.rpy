# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define phone = Character("Phone")
define mom = Character("Mom")
define jj = Character("Java Joe")


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

    mc "Alright, let's get to work!"

    phone "Buzz, buzz... New text from Mom!"

    mc "What does she want now?"

    mom "[mc] are you still coming to the wedding?"

    mom "Your sister wanted to know."

    mc "She could've text me directly..."

    mom "She thinks you hate her after she didn't include you in the wedding."

    mom "Anyways! Make sure to bring a date! That is your sister's one request"

    mc "Why does she care?"

    mom "She just wants you to have a good time."

    mc "Why do I need a date to have a good time?"

    mom "Don't make this so difficult... just bring a date. It'll make your sister happy!"

    mc "Fine..."

    mc "I guess that means I need to find someone to go with. But I need to get to work! I'm already late."

    # MC makes it to the coffee shop, it's time themed
    jj "[mc]! Where have you been? You're 7 minutes and 46 seconds late."

    menu where_been:
        "..."
        "I don't have to explain myself to you, Java Joe.":
            jj "What's with the attitude?"

        "My mom was texting me. She wants me to find a date.":
            jj "You know, that's not a valid excuse to be late."

        ""

    jj "Well, anyways, we need you back here. The morning rush is about to come and-"

    cm "BBBRRRRRRRRRRRRRRRRRRRRRR"

    jj "And we need you."

    mc "What's with that noise?"

    jj "It's a new espresso machine."

    mc "Are you sure it's new...?"

    jj "It is new. The packaging said after some uses it won't be that loud anymore."

    jj "Don't worry about the sound though. It's loud, so if you don't hear a customer, just ask them to repeat themselves."

    mc "Alright..."

    # SHIFT 1: START
    # Bad ending: getting fired for messing up orders

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
