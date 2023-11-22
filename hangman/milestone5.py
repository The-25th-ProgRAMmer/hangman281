import random

class Hangman: 
    def __init__(self, word_list, num_of_lives=5):

        #List of words that will be loaded into the class. 
        self.word_list = word_list

        #The word to be guessed, picked randomly from the word_list passed in. 
        self.word = random.choice(self.word_list)

        #A list of the letters of the word, with _ for each letter not yet guessed. 
        # For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. 
        # If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        #Designed to be reactive to the word chosen, i.e if apple then = ['a', 'p', '_', '_', '_' ]
        self.word_guessed = ["_" for letter in self.word]

        #The number of UNIQUE letters in the word that have not been guessed yet
        self.num_letters = len(self.word)

        #The number of lives the player has at the start of the game.
        self.num_lives = num_of_lives

        # A list of the guesses that have already been tried. Empty intially 
        self.list_of_guesses = []



    
    '''
    checks if the letter passed in is in the word chosen by the random function.
    if so, the word is assigned to the word_guessed list in the correct place and then the no.of letters is reduced by 1 
    Letter assignment is done via an enumerate method. 

    If not the chosen letter, reduce the num_of_letters and ask for another input. 

    '''
    def check_guess(self, letter):

        guessed_letter = letter.lower() 
    
        if guessed_letter in self.word:
            print(f"Good guess! {guessed_letter} is in the word.")

            for index, letter in enumerate(self.word):
                if letter == guessed_letter:
                    self.word_guessed[index] = letter
                    self.num_letters -=  1 
                
        else: 
            self.num_lives -= 1  

            print(f"Sorry, {guessed_letter} is not in the word. Try again")
            print(f"You have {self.num_lives} remaining!")

    
    '''
    Keep accepting inputs and if already chosen, ask to chose again. 
    Character checking utilised and append it to the self.guessed_list.

    '''
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

                #jumps out of the loop once an input is taken. Important. 
                break


def play_game(word_list): 

    #intialize with 5 lives and create a game object. 
    #Loop until conditions are fufilled. 

    num_lives = 5 
    game = Hangman(word_list, num_lives)


    while True:
         
         print(game.word_guessed)
         #print(game.num_letters)

         if game.num_lives == 0: 
             print("You have lost, try again")
             break
        
         if game.num_letters == 0: 
             print("Congratulations, you have won!")
             break

         game.ask_for_input()
        
  

play_game(["apple"])


