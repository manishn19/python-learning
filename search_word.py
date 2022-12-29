# Search a word in a santance

santance_text = "Lorem ipsum simply dummy text lorem"
word = "Lorem"

# case sensitive word 
if word in santance_text:
    count = santance_text.count(word)
    print(f'word found (case sensitive) {count} times')
else:
    print('word not found (case sensitive)')


# not case sensitive
if word.lower() in santance_text.lower():
    count = santance_text.lower().count(word.lower())
    print(f'word found {count} times')
else:
    print('word not found')