# find the word in the string

word = 'Binmile'
user_input = "mdslkmfafdlaoldnmcidlsiyeljgddsdoljsejhb"
string_list = [*user_input] # convert string to a list
word_list = [letter for letter in word]
matching_word = ''
for letter in word:
    if letter.lower() in user_input:
        matching_word += letter

if matching_word == word:
    print('Word matching')
else:
    print('Word not matching')


print(matching_word)