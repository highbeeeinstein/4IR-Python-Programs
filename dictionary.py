dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
#dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# for english, french in dictionary.items():
#     print(english, "->", french)
dictionary['cat'] = 'minou'
dictionary['swan'] = 'cygne'
dictionary.update({"duck": "canard"})
del dictionary['dog']
dictionary.popitem()
print(dictionary)