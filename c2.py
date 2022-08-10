from MergeSort import mergeSort
import time
from OptionScreen import display_options

def choice_2(our_dictionary):
    list_of_keys = list(our_dictionary.keys())
    if len(list_of_keys) != 0:
        mergeSort(list_of_keys)
        print('Available list: ')
        print(list_of_keys)
    else:
        print("Sorry! the list of words is empty")
    time.sleep(3)
    global number
    number = display_options()