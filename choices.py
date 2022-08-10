from MergeSort import mergeSort
from BinarySearch import binarySearch
import time
from OptionScreen import display_options



def choice_2_b(our_dictionary):
    list_of_keys = list(our_dictionary.keys())
    if len(list_of_keys) != 0:
        mergeSort(list_of_keys)
        print('Available list: ')
        print(list_of_keys)
    else:
        print("Sorry! the list of words is empty")
    time.sleep(3)




def choice_3_b(our_dictionary):
    # add a new word
    key = input("Add new Word: ")
    value = input("Add an appropriate hint: ")
    new_dictionary = {key: value}
    our_dictionary.update(new_dictionary)
    newList = list(our_dictionary.keys())
    global sorted_list
    sorted_list = mergeSort(newList)
    time.sleep(2)

def choice_4_b(our_dictionary):
    element = input("Enter a word to remove it from dictionary: ")
    list_key = list(our_dictionary.keys())
    mergeSort(list_key)

    x = binarySearch(list_key, 0, len(list_key) - 1, element)

    if x == True:
        del our_dictionary[element]
    else:
        print("Word not Found")

    time.sleep(3)

def choice_5_b(our_dictionary):
    element = input("Enter a word you wish to change its hint: ")
    modified_hint = input("Enter a modified hint: ")

    list_key = list(our_dictionary.keys())
    mergeSort(list_key)

    x = binarySearch(list_key, 0, len(list_key) - 1, element)

    if x == True:
        our_dictionary[element] = modified_hint
        print(our_dictionary)
    else:
        print("Word not Found")

    time.sleep(3)