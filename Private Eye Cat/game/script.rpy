# The script of the game goes in this file.

## Menu Splashscreen
## source: https://www.renpy.org/wiki/renpy/doc/cookbook/Adding_a_Splashscreen
    ## note: fix parallax, as the layers boot up one by one from splashscreen

label splashscreen:
    scene black
    with Pause(1)

    show text "Helwa H Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define MC = Character("Marley", image="MC")
define B = Character("The Bartender")
define F = Character("???")

image side MC normal = "side MC normal.png"

# sprite anims
image Bartender:
    "Bartender Normal.png"
    0.21
    "Bartender Normal 2.png"
    0.21
    "Bartender Normal 3.png"
    0.21
    repeat
image Bartender Speak:
    "Bartender Normal.png"
    0.21
    "Bartender Speak 1.png"
    0.21
    "Bartender Speak 2.png"
    0.21
    repeat

image Fang:
    "Fang Normal 1.png"
    0.21
    "Fang Normal 2.png"
    0.21
    "Fang Normal 3.png"
    0.21
    repeat
image Fang Speak:
    "Fang Speak 1.png"
    0.21
    "Fang Speak 2.png"
    0.21
    "Fang Normal 1.png"
    0.21
    repeat



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    scene black bg
    with fade

    play music "535776__breviceps__distant-ambulance-fire-truck-sirens-germany.wav" volume 0.5 fadein 2.0
    
    ## temp until I come up with something better...
    F "Its no use! We can't save them Marley!"
    F "Yes I can! If I don’t then they'll never get back to—"



    scene bar bg
        # https://en.idei.club/32182-bar-background.html
    play music "piano-bar-piano-lounge-background-chill-music-4178.mp3" volume 0.5
        # https://pixabay.com/music/acoustic-group-piano-bar-piano-lounge-background-chill-music-4178/
    show Bartender Speak
    with fade

    B "Something on your mind again?"

    show Bartender

    MC normal "Ah– no not really, just spacing out…"

    show Bartender Speak

    B "You sure? You’ve been coming an awful lot in here, aren't you a detective? Shouldn't you be stopping bad guys or whatnot?"

    show Bartender

    MC "I'm not a cop, my work is different, you should know that by now."

    MC "It's just business has been slow, that's all."

    show Bartender Speak

    B "Hah! Well the city has been much better after that one case..."

    B "What was it called again? Ah well..."

    B "That case should've brought in more clients for ya! Then again, it affected the lives of so many other cats here–"

    show Bartender

    MC "Boss, another cup. Add in a can too."

    MC "(The Bartender paused for a bit. He stared at me, but shrugged it off quickly.)"
    
    MC "(I didn't want to talk about that case, in fact I would rather forget everything about it.)"

    MC "(That case was affecting the lives of all, both during and after it closed...)"

    stop music

    show Bartender Speak

    B "Umm…"

    show Bartender

    MC "..?"

    MC "Is there something wrong?"

    show Bartender Speak

    B "Haha! Well, we’re out of it."

    show Bartender

    MC "You mean…?"

    MC "(He can't be serious, is he really out of what I think it is–)"

    # change music here

    show Bartender Speak

    B "We’re out of cans, canned tuna."

    show Bartender

    MC "...!"

    play music "piano-bar-piano-lounge-background-chill-music-4178.mp3" volume 0.5
        # https://pixabay.com/music/acoustic-group-piano-bar-piano-lounge-background-chill-music-4178/

    show Bartender Speak
    
    B "I've been having a hard time getting in new stock, even when I call my supplier he just gives me strange answers every time…"

    show Bartender

    MC "I see..."

    with fade

    MC "(I need some answers)"

    menu:
         
        "“What strange answers is your supplier giving you?”":
            jump strange

        "“Can you just get more?”":
            jump more

        "“Do you have canned chicken?”":
            jump chicken

    label strange:
        MC "What “strange” answers is your supplier telling you?"

        show Bartender Speak

        B "They’re telling me that they sold all of it to another client! Can you believe that?"

        B "They won't even tell me who the other feline is!"

        B "{color=#00ff00}Why would they need THAT many canned tunas for?{/color}"

        show Bartender

        MC "I see..."

        MC "Put it on my tab, I'm heading out"

        scene black bg
        with fade

        stop music

        jump ActOne

    label more:
        MC "Can you just, like, get more?"

        show Bartender Speak

        B "Do you have ear mites? I just told you why!"

        show Bartender

        MC "Ah right, my mistake..."

        MC "Boss, put it on my tab. I'm heading out"

        scene black bg
        with fade

        stop music

        jump ActOne

    label chicken:
        MC "Do you have canned chicken instead?"

        show Bartender Speak

        B "Let me check…"

        show Bartender

        B "..."

        show Bartender Speak

        B "Looks like we got some!"

        scene black bg
        with fade

        stop music

        jump gameOver
    
    label ActOne:
        play music "705207__klankbeeld__summer-night-suburb-nl-2.mp3" volume 0.5 fadein 1.0
        # https://freesound.org/people/klankbeeld/sounds/705207/

        scene night sky bg
        with fade

        "The night is quite cold..."

        "Should've brought a thicker coat..."

        scene street night bg
        with dissolve

        MC normal "I need to head back to my office"

        MC "But, I could really use a cat nap right now..."

        play music "493741__the-sacha-rush__wide-cinematic-ambiet-for-tension-effect.mp3" volume 0.5 fadeout 1.0
        # https://freesound.org/people/The-Sacha-Rush/sounds/493741/

        scene fang cg1
        with fade

        "...!"

        scene fang cg2
        with dissolve

        "...?"

        scene street night bg
        with fade

        play music "579575__szegvari__dance-lofi-techno.mp3" volume 0.3 fadein 1.5
        # https://freesound.org/people/szegvari/sounds/579575/

        show Fang Speak
        with dissolve

        F "Meowdy"

        show Fang

        MC normal "...!"

        show Fang Speak

        F "Whats with the face?"

        show Fang

        F "..."

        show Fang Speak

        F "Its rude to stare nya know?"

        show Fang

        MC "Im sorry, I didnt mean--"

        MC "(Wait...)"

        MC "(Something is odd...)"

        MC "(Something smells {b}fishy{/b})"

        show Fang Speak

        F "Hello? You speak catlish?"

        F "Has something caught your eye...?"

        stop music

        scene tunaed
        window hide dissolve
        pause 5.0

        

        return

    label gameOver:
        " Game Over "

        return

    # This ends the game.

    return
