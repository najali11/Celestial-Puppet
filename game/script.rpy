# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Null", image="null")
define b = Character("Blanche", image="blanche")

define in_eye = ImageDissolve("/dissolvers/eye.png", 6.0)
define out_eye = ImageDissolve("/dissolvers/eye.png", 6.0, reverse=True)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    show bluesky

    "The boundless snow beneath my feet."
    "The blazing sun above my head."
    "I seem to see the celestial palanquin running in the sky."
    "Heading to a place..."
    "...Far, far away."
    "There are souls in this place, untethered to the connections they formed in the realm below."
    "Soon they will enter life again."
    "Forever bound to this karmic cycle."
    hide bluesky
    "That is the time we have left in this temporary realm before we are forced to reincarnate."
    "Before we reincarnate, we can enter a contract with an Impermanence."
    "They are guardians of the overworld, entrusted with the task of overseeing mortal reincarnation."
    "Entering a contract is not difficult. However, many have failed to live up to the contract."
    "This is because the contract removes our memories of our original wish while dooming us to lifetimes of tribulations."
    "After the end of each life, we have the option to forego our contracts."
    "Many people choose to forgo."
    "Because their purpose has already been lost."
    "For me, this is already my 20th lifetime in."
    "It seems my wish must have been a grand one that I was willing to sacrifice 50 lifetimes to achieve it."
    "The minutes are counting down. It seems my time here is soon up."
    

    # These display lines of dialogue.

    # This ends the game.

    return
