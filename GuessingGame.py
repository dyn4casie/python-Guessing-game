# This is a guessing the number game.
import random

# User's name
print("Wadup! What is your name? \n")
myName = input()
print("\n-------------------------------------------------------------\nHi " + str(myName) + "!" + " Let's play a guessing game.")


def random_game():

    play = True
    while play:

        easy = random.randint(1, 10)
        medium = random.randint(1, 20)
        hard = random.randint(1, 50)
        # select a difficulty to play on
        print("Would you like to play on easy, medium, or hard?"
              "\nType 'easy' for Easy, 'medium' for Medium, or 'hard' for Hard!\n--------------------------------------------------------------")

        level_selection = True
        while level_selection:
            level = input()
            if level == "easy":
                print("Awwww, i see you are lily-Livered.\n ")
                level_selection = not True
                break
            if level == "medium":
                print("Hehehe...Still not brave enough.\n")
                level_selection = not True
                break
            if level == "hard":
                print("Hmmmm...Respect Legend, Hope this is tough enough.\n")
                level_selection = not True
                break
            else:
                print("Invalid input!\nPlease enter either easy, medium, or hard. ")


    # If the user selects e for Easy - 6 tries
        if level == 'easy':
            print("Because you selected easy, you'll have 6\nguesses to guess a number between 1-10.")
            guesses_left = 6
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == easy:
                    print("That's it, you've guessed the right number! " + str(easy))
                    print("You got it right " + str(myName) + "!")
                    break
                elif try1 < easy:
                    print("That was wrong!")
                elif try1 > easy:
                    print("That was wrong!")
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                # Fun 5 tries left count down
                if guesses_left == 5:
                    print("Common', you can do this!\n")
                if guesses_left == 4:
                    print("That's ok, it's on Easy.\n")
                if guesses_left == 3:
                    print("You're running out of guesses!\n")
                if guesses_left == 2:
                    print("Just 2 guesses left. Can the impossible happen?\n")
                if guesses_left == 1:
                    print("By the old Gods and the New.\nYou've got 1 guess left.\n😨")

                # If the user runs out of guesses
                if guesses_left == 0:
                    print("Game OVer!\n")

    # If the user selects m for Medium - 10 tries
        if level == 'medium':
            print("Because you selected medium, you'll have 4\nguesses to guess a number between 1-20.")
            guesses_left = 4
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == medium:
                    print("That's it, you've guessed the right number! " + str(medium))
                    print("You got it right " + str(myName) + "!")
                    break
                elif try1 < medium:
                    print("That was wrong!")
                elif try1 > medium:
                    print("That was wrong!")
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                # Fun 3 tries left count down
                if guesses_left == 3:
                    print("You're running out of guesses!\n")
                if guesses_left == 2:
                    print("Just 2 guesses left. Can the impossible happen?\n")
                if guesses_left == 1:
                    print("By the old Gods and the New.\nYou've got 1 guess left.\n😨")

                # If the user runs out of guesses
                if guesses_left == 0:
                    print("Game Over!\n")

    # If the user selects h for Hard - 3 tries
        if level == 'hard':
            print("Because you selected hard, you'll have 3\nguesses to guess a number between 1-50.")
            guesses_left = 3
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == hard:
                    print("That's it, you've guessed the right number! " + str(hard))
                    print("You got it right " + str(myName) + "!")
                    break
                elif try1 < hard:
                    print("That was wrong!")
                elif try1 > hard:
                    print("That was wrong!")
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                # Fun 4 tries left count down - 5 won't work for hard because you begin at 5
                if guesses_left == 2:
                    print("Just 2 guesses left. Can the impossible happen?\n")
                if guesses_left == 1:
                    print("By the old Gods and the New.\nYou've got 1 guess left.\n😨")

                # If the user runs out of guesses
                if guesses_left == 0:
                    print("Game Over!")

        maybe_play = True
        while maybe_play:
            again = input("\nWould you care to play again?\nYes or No\n ")
            if again == "No" or again == "no":
                print('\nOk, thank you for playing.\nFeel free to come back any time!')
                maybe_play = not True
                play = not True
            elif again == "yes" or again == "Yes":
                print("\nCool, let's play again!👍\n")
                maybe_play = not True
                play = True
            else:
                print("Please enter either yes or no.")
                input()
                maybe_play = not True
                play = not True


random_game()

