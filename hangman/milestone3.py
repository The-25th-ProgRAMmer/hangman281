
import milestone2 

def check_guess(guess):

    guess_chr = guess.lower() 
    
    if guess_chr in milestone2.random_fruit: 
        print(f"Good guess! {guess} is in the word.")
    else: 
        print(f"Sorry, {guess} is not in the word. Try again")


def ask_for_input(guess): 

    check_guess(guess)

    while True: 
        if guess.isalpha() == True: 
            break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")


ask_for_input("A")