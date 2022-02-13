from MergeSort import mergeSort
from BinarySearch import binarySearch
from OptionScreen import Loading_function, color
import time


def choice_2_b(our_dictionary):
    Loading_function()
    list_of_keys = list(our_dictionary.keys())
    if len(list_of_keys) != 0:
        mergeSort(list_of_keys)
        print('Available list: ')
        print(color.PURPLE + str(list_of_keys) + color.END)
    else:
        print("Sorry! the list of words is empty")
    time.sleep(3)


def choice_3_b(our_dictionary):
    Loading_function()
    key = input("Add new Word: ")
    value = input("Add an appropriate hint: ")
    new_dictionary = {key: value}
    our_dictionary.update(new_dictionary)
    Loading_function()
    time.sleep(1)


def choice_4_b(our_dictionary):
    Loading_function()
    element = input("Enter a word to remove it from dictionary: ")
    list_key = list(our_dictionary.keys())
    mergeSort(list_key)

    result = binarySearch(list_key, 0, len(list_key) - 1, element)

    Loading_function()
    if result:
        del our_dictionary[element]
    else:
        print("Word not Found")

    time.sleep(1)


def choice_5_b(our_dictionary):
    Loading_function()
    element = input("Enter a word you wish to change its hint: ")
    modified_hint = input("Enter a modified hint: ")

    Loading_function()
    list_key = list(our_dictionary.keys())
    mergeSort(list_key)

    x = binarySearch(list_key, 0, len(list_key) - 1, element)

    if x:
        our_dictionary[element] = modified_hint
    else:
        print("Word not Found")

    time.sleep(1)


def choice_7_b(our_dictionary, dic_path):
    wish = input('do you wish to save the changes [y/n]? ')
    if wish == 'y':
        our_dictionary_file_0 = open(dic_path, 'w')
        for k, val in our_dictionary.items():
            our_dictionary_file_0.write(k + ':' + val + '\n')
        time.sleep(0.7)
        print(color.PURPLE + 'ok...' + color.END)
        time.sleep(0.7)
        print(color.PURPLE + 'Goodbye 😴' + color.END)
        time.sleep(0.7)
    else:
        time.sleep(0.7)
        print(color.PURPLE + 'Your loss...' + color.END)
        time.sleep(0.7)
        print(color.PURPLE + 'Goodbye 😴' + color.END)
        time.sleep(0.7)
