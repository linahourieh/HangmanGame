from MergeSort import mergeSort
import time
from OptionScreen import display_options
def choice_3(our_dictionary):
    # add a new word
    key = input("Add new Word: ")
    value = input("Add an appropriate hint: ")
    new_dictionary = {key: value}
    our_dictionary.update(new_dictionary)
    newList = list(our_dictionary.keys())
    global sorted_list
    sorted_list = mergeSort(newList)
    time.sleep(2)
    global number
    number = display_options()
