dic_path = '/home/lina/PycharmProjects/HangmanGame/our_dictionary.txt'
our_dictionary = {}
our_dictionary_file = open(dic_path,'r')


for line in our_dictionary_file:
    key, value = line.split(":")
    value = value.strip()
    our_dictionary[key] = value


#print(our_dictionary)


options = 'Welcome to HangMan game 😄' \
          'Please choose one of the following option'
          '\n1. Play Hangman ' \
          '\n2. List Words in Dictionary ' \
          '\n3. Add Word to Dictionary ' \
          '\n4. Remove Word from Dictionary ' \
          '\n5. Change Word Hint' \
          '\n6. Exit'

print(options)