import string, random

#great to create our own functions, 5 separate random letters for 5 random variables
def generator():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    letter4 = random.choice(string.ascii_lowercase)
    letter5 = random.choice(string.ascii_lowercase)


#lets ask the user for some input

letter_input_1 = input('choose a letter..."v" for vowels , "c" for consonants , "l" for any other letter')
letter_input_2 = input('choose a letter..."v" for vowels , "c" for consonants , "l" for any other letter')
letter_input_3 = input('choose a letter..."v" for vowels , "c" for consonants , "l" for any other letter')
letter_input_4 = input('choose a letter..."v" for vowels , "c" for consonants, "l" for any other letter')
letter_input_5 = input('choose a letter..."v" for vowels , "c" for consonants , "l" for any other letter')

#now lets put some conditional
#we have to create a condition vowels and consonants because python doesnt have them built in

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letter = string.ascii_lowercase

if letter_input_1 == "v":
    letter1 = random.choice(vowels)
elif letter_input_1 == "c":
    letter1 = random.choice(consonants)
elif letter_input_1 == "l":
    letter1 = random.choice(letter)
else:
    letter1 = letter_input_1#allow user to choose any letter











