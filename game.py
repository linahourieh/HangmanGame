import time, random
from OptionScreen import Loading_function, color
from drawings import draw_hangman




def score_calculate(masked, dashes = 0):
    for d in masked:
        if d == '-':
            dashes += 1
    score = (len(masked) - dashes) * 100 // len(masked)
    return score

def play(our_dictionary):
    time.sleep(0.7)
    name = input("What is your name? ")
    print(f"Hello {color.PURPLE + name + color.END}, let's play hangman!")
    

    time.sleep(0.7)
    Loading_function()

    # Return a random element from a list
    list_key = list(our_dictionary.keys())

    word = random.choice(list_key)
    hint = our_dictionary[word]
    trials = 8

    print(f"Your hint will be: {color.PURPLE + hint + color.END}")
    time.sleep(2)

    print(f"You have only {color.PURPLE + str(trials) + color.END} trials before you get killed 🔪")
    time.sleep(2)
    print("Oh, no I'm kidding.")
    time.sleep(2)
    masked = "-" * len(word)
    print("'", masked, "'")
    time.sleep(0.7)
    draw_hangman(0)
    time.sleep(0.7)
    print("start")


    def replace_char_at_index(org_str, index, replacement):
        if index < len(org_str):
            org_str = org_str[0:index] + replacement + org_str[index + 1:]
        return org_str

    while trials > 0:
        if '-' not in masked:
            print(score_calculate(masked))
            print("you won")
            break
        else:
            time.sleep(0.7)
            character = input('Guess a character: ')
            time.sleep(0.7)
            print(color.PURPLE+'_______________________________________________'+color.END)

            idx_list = []
            for k in range(len(word)):
                if word[k] == character:
                    idx = k
                    idx_list.append(idx)

                else:
                    continue

            if len(idx_list) != 0:
                for index_ in idx_list:
                    masked = replace_char_at_index(masked, index_, character)
                time.sleep(2)
                print(f"You still have {color.PURPLE + str(trials) + color.END} trials.")
                time.sleep(0.7)
                print("[", masked, "]")
                time.sleep(0.7)
                draw_hangman(8-trials)

            else:

                trials -= 1
                time.sleep(2)
                print(f"You have only {color.PURPLE + str(trials) + color.END} trials left.")
                time.sleep(0.7)
                print("'", masked, "'")
                time.sleep(0.7)
                draw_hangman(8-trials)
    else:
        print("oops, you lost")
        print(score_calculate(masked))
        time.sleep(2)
        print("RUN...")

    time.sleep(2)