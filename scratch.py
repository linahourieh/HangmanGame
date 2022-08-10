from Hash_table import HashTable as HT



# import the dictionary file
dic_path = 'our_dictionary_hashed.txt'
our_dictionary_1 = {}
our_dictionary_file = open(dic_path, 'r+')

# parse the file
for line in our_dictionary_file:
    key, value = line.split(":")
    value = value.strip()
    our_dictionary_1[key] = value

print(our_dictionary_1)


t = HT(100)


print(our_dictionary_1.values())

for i in range(len(our_dictionary_1.keys())):
    HT.add(t, list(our_dictionary_1.keys())[i], list(our_dictionary_1.values())[i])

print(t)

print(HT.get(t, 'tomato'))