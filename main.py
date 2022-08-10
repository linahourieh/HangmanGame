import time

from OptionScreen import display_options, example_0,example_1, description
from choices import choice_2_b, choice_3_b, choice_4_b, choice_5_b
from game import play

# import the dictionary file
dic_path = 'our_dictionary.txt'
our_dictionary = {}
our_dictionary_file = open(dic_path, 'r+')

# parse the file
for line in our_dictionary_file:
    key, value = line.split(":")
    value = value.strip()
    our_dictionary[key] = value

# display_options & take input number from the user
global number
number = display_options()


# defining the choices a user would make
def HangMan():
    play(our_dictionary)
    global number
    number = display_options()


def choice_2():
    choice_2_b(our_dictionary)
    global number
    number = display_options()


def choice_3():
    choice_3_b(our_dictionary)
    global number
    number = display_options()


def choice_4():
    choice_4_b(our_dictionary)
    global number
    number = display_options()


def choice_5():
    choice_5_b(our_dictionary)
    global number
    number = display_options()


def choice_6():
    description(1)
    description(2)
    example_0()
    description(3)
    example_1()
    global number
    number = display_options()


def choice_7():
    print('GOODBYE')
    exit


# a while loop to keep getting back into the display options screen
while number != 7:
    if number == 1:
        HangMan()
    elif number == 2:
        choice_2()
    elif number == 3:
        choice_3()
    elif number == 4:
        choice_4()
    elif number == 5:
        choice_5()
    elif number == 6:
        choice_6()
else:
    choice_7()
