import string
#print(help(string))
print(string.ascii_letters)
print(string.ascii_lowercase)

#we want a random selection hence the random module
import random
print(random.choice('pull a string from here'))
print(random.choice(string.ascii_lowercase))


