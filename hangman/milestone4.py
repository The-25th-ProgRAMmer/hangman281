import random

class Hangman: 
    def __init__(self, word_list, num_of_lives=5):

        
        #List of words
        self.word_list = word_list

        #The word to be guessed, picked randomly from the word_list. 
        self.word = random.choice(self.word_list)

        #A list of the letters of the word, with _ for each letter not yet guessed. 
        # For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. 
        # If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        self.word_guessed = ["_" for i in range(len(self.word))]

        #The number of UNIQUE letters in the word that have not been guessed yet
        self.num_letters = len(self.word)

        #The number of lives the player has at the start of the game.
        self.num_lives = num_of_lives

        # A list of the guesses that have already been tried. Set this to an empty list initially
        self.list_of_guesses = []

    def check_guess(self, letter):

        guessed_letter = letter.lower() 
    
        if guessed_letter in self.word:
            print(f"Good guess! {guessed_letter} is in the word.")

            for letter in self.word:
                if letter == guessed_letter:
                    index = self.word_guessed.index("_")
                    self.word_guessed.insert(index, letter)
            self.num_letters -=  1 

        else: 
            self.num_lives -= 1
            print(f"Sorry, {guessed_letter} is not in the word. Try again")
            print(f"You have {self.num_lives} remaining!")

    
    def ask_for_input(self):

        while True: 
            
            #print(self.word_guessed)
            #print(self.list_of_guesses)
            
            guess = input("Please enter letter: ")

            if guess.isalpha() != True: 
                print("Invalid letter. Please, enter a single alphabetical character.")

            elif guess in self.list_of_guesses:
                print("You already tried that letter")

            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


hangman = Hangman(["apple", "fruit", "canteloupe"])
hangman.ask_for_input()

        
            


