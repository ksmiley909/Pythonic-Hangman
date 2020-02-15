#Pythonic Hangman

import random
#import string

WORD_FILE = "wordlist.txt"

alphabet = "abcdefghijklmnopqrstuvwxyz-"

letter_list = list(alphabet)


#Read and convert text file to list of strings.  From list, select word at random.
def choose_word():              
    print ('Gathering Words...')
    masked_word = (random.choice(open('wordlist.txt').read().split()))
    return masked_word

#Determine whether or not the player has succesfully guessed the word
def is_word_guessed(masked_word, letters_guessed):

    isguessed = False
    for q in masked_word:
        if q in letters_guessed:
            isguessed = True
        else:
            isguessed = False
            break
    return isguessed
    
   
#Disguise word.  Reveal correctly guessed letters
def get_guessed_word (masked_word, letters_guessed): 
    guessed_word = ''
    for q in masked_word:
        if q in letters_guessed:
            guessed_word += q+' '
        else:
            guessed_word += ' _ '
    return guessed_word


#Show player letters not yet guessed
def selected_letter_tracker(letters_guessed):
    available = ""

    for k in letters_guessed:
        available += k 
        
    
    for t in letter_list:
        if t in letter_list:
            letter_list.remove(t) 
        return available
    

#Primary game loop w/ rules, descending attempt counter, and record of characters guessed
def hangman(masked_word):

    guesses = 16
    letters_guessed = list()

    print("Welcome to Hangman!\n")
    print("You have 16 guesses.  Alphabetical Characters Only.\n Invalid Characters Cost One Turn")
    print("Begin! Your word is:",len(masked_word), "letters long:\n",get_guessed_word(masked_word, letters_guessed))
    print("\nAvailable Characters:", alphabet)


    
    while(guesses>0):

        letter = input('Guess a Letter:  ')

        if letter not in alphabet:
            guesses -=1
            print("Available Characters Only!",alphabet)
            print("You have", guesses, "guesses left") 
      
        else:
            if letter in letters_guessed:
                guesses -=1
                print("You've used this letter already!", get_guessed_word(masked_word, letters_guessed))
             
            else:
                letters_guessed.append(letter)
                if letter in masked_word:
                    guesses -=1
                    print("Good Guess!:",get_guessed_word(masked_word, letters_guessed))
                if letter not in masked_word: 
                        guesses -=1
                        print("Bummer!  That letter is not in the word!",get_guessed_word(masked_word, letters_guessed))
                        
            if is_word_guessed( masked_word,letters_guessed):
                print("YOU WIN!")
                print("The word is:", masked_word)
                break               
                           
                          
            print("You have", guesses, "guesses left")
            print("Characters Tried:", selected_letter_tracker(letters_guessed))

        if guesses==0 and not is_word_guessed( masked_word, letters_guessed):
                print("YOU LOSE!")
                print("The word is:", masked_word)
                break

        
      

hangman(choose_word())




            
                                        
                                                                               
                                                                               
