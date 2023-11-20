import random

new_list = ["apple", "mango", "pear", "orange", "pineapple"]
word = random.choice(new_list)
guess = input(" ")

if len(guess) == 1 and guess.isalpha(): 
    print("Good Guess")
else: 
    print("Oops! That is not a valid input.")


#print(new_list)
print(guess)
#print(word)
