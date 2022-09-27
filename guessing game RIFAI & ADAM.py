import random 

def main():
    """Let's start guessing elements and numbers of periodic table game."""
    print("Guess the elements !")

"""line ini berfungsi untuk senarai jadual berkala"""
    periodic = [
        "hydrogen",
        "helium",
        "lithium",
        "beryllium",
        "boron",
        "carbon",
        "nitrogen",
        "oxygen",
        "fluorine",
        "neon",
        "sodium",
    ]

"""x ialah pilihan secara rawak daripada jadual berkala"""
    x = random.choice(periodic)
    print(x)

"""guess ialah pemain """
    guess = None
    
    while x != guess:

        guess = str(input("what element do i think ?"))


        if x == guess:
            print("You guessed {}. congratulation you get it right!".format(guess))
        elif x == "hydrogen":
            print("is a gas of diatomic molecules having the formula H2.")
        elif x == "helium":
            print("is a chemical element with the symbol He and atomic number 2.")
        elif x =="lithium":
            print("is soft and silvery white and it is the least dense of the metals.")
        elif x == "beryllium":
            print("is a steel gray and hard metal that is brittle at room temperature.")
        elif x == "boron":
            print("It’s a poor conductor of electricity and can also be found in flare guns, and fiber glasses.")
        elif x == "carbon":
            print("is a non-metallic element which occurs in various forms.")
        elif x == "nitrogen":
            print("Nitrogen is an odorless, colorless and tasteless gas that makes up 80% of the air we breathe.")
        elif x == "oxygen":
            print("for chemical reactions that keep the body alive, including the reactions")
        elif x == "fluorine":
            print( "Fluorine is the most reactive and the most electronegative of all the elements.")
        elif x == "neon":
            print("")
        elif x == "sodium":
            print(" It is a soft, silvery-white, highly reactive metal.")


main()
