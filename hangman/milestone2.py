import random

list_of_fruits = ["apple", "mango", "pear", "orange", "pineapple"]
random_fruit = random.choice(list_of_fruits)
letter_guess = input(" ")

if len(letter_guess) == 1 and letter_guess.isalpha(): 
    print("Good Guess")
else: 
    print("Oops! That is not a valid input.")


#print(new_list)
print(letter_guess)
#print(word)
