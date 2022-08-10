import shutil
import sys
import time


# A class implemented for using colors
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# columns were used to push the string to the middle
columns = shutil.get_terminal_size().columns


# used to display multiple options
def display_options():
    time.sleep(0.7)
    print('---------------------------------------------------------------------'.center(columns))
    print(color.PURPLE + color.BOLD + 'WELCOME !'.center(columns) + color.END)
    print('---------------------------------------------------------------------'.center(columns))
    time.sleep(0.7)
    options = 'Welcome to the HangMan game:😄\n1. Play Hangman \n2. List Words in Dictionary \n3. Add Word to ' \
              'Dictionary \n4. Remove Word from Dictionary \n5. Change Word Hint\n6. Help\n7. Exit '
    print(options)
    print('-------------------------------------------------------------------------'.center(columns))
    time.sleep(0.7)
    number = int(input("choose a number: "))
    return number


# used to draw loading line
def Loading_function():
    print()
    print(color.PURPLE + "Loading:" + color.END)

    animation = [color.PURPLE +
                 "[■■□□□□□□□□□□□□□□□□□□]",
                 "[■■■■□□□□□□□□□□□□□□□□]",
                 "[■■■■■■□□□□□□□□□□□□□□]",
                 "[■■■■■■■■□□□□□□□□□□□□]",
                 "[■■■■■■■■■■□□□□□□□□□□]",
                 "[■■■■■■■■■■■■□□□□□□□□]",
                 "[■■■■■■■■■■■■■■□□□□□□]",
                 "[■■■■■■■■■■■■■■■■□□□□]",
                 "[■■■■■■■■■■■■■■■■■■□□]",
                 "[■■■■■■■■■■■■■■■■■■■■] " + color.END]

    for i in range(len(animation)):
        time.sleep(0.4)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")


def description(num):

    if num == 1:
        print("The computer first selects a secret word at random from a list built into the game. \n" \
            "The game then prints out a row of dashes, each one represents a letter in the secret word. \n" )
    elif num == 2:
        print("The game asks the user to guess a letter. \n" \
              "If the user guesses a letter that is in the word, the word is redisplayed with all instances of " \
              "that letter shown in the correct positions, along with any letters correctly guessed on previous turns.\n")
    else:
        print("If the letter does not appear in the word, the user is charged with an incorrect guess. ")


def example_0():
    example_0_list = ['---', 'c--', 'c-t', 'cat']
    for i in range(len(example_0_list)):
        time.sleep(0.3)
        sys.stdout.write("\r" + example_0_list[i % len(example_0_list)])
        sys.stdout.write('   trails 2')
        sys.stdout.flush()
    time.sleep(0.3)
    print("    ***You Won!***    ")


def example_1():
    example_1_list = ['---', 'c--', 'c-t']
    for i in range(len(example_1_list)):
        time.sleep(0.3)
        sys.stdout.write("\r" + example_1_list[i % len(example_1_list)])
        sys.stdout.write(f'   trails {len(example_1_list) - 2 - i + 1}')
        sys.stdout.flush()
    time.sleep(0.3)
    print("    ***Game Over***    ")


def examples():
    example_0()
    example_1()
    time.sleep(2)
