# input from the user
# check the palindrom from user input 

user_input = input('Type the text to check the Palindrome: ')
palindrome = user_input[::-1]
if user_input == palindrome:
    print('Plindrome')
else:
    print('Not palindrome')
