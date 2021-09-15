import random


def read_file(file_name):
    short_words = open(file_name) # opens file
    list = short_words.readlines() # reads text in textfile
    short_words.close() # closes text file 
    
    return list # returns text file for later use


def select_random_word(file_name):
    underscore = '_' 
    choser = random.randint(0, len(file_name)-1) # returns a random interger from the randomly chosen word
    word_choser = file_name[int(choser)] # chooses a a random word from the text file
    word_strip = str(word_choser) # turns the word into string
    word_string = list(word_strip) # contains the text file list
    random_postition = random.randint(0, len(word_string)-2) # choses a random letter to be the missing letter
    word_string[random_postition] = underscore # makes the random letter as an underscore
    word = ''.join(word_string) # adds the intergers as letters instead of an underscore
    print('Guess the word: ' +word) # prints out 'Guess the word'
 
    return word_choser # returns a randomly chosen word every time the code runs


def get_user_input():
    user = input('Guess the missing letter: ') # gives the user a chance to answer the question
    
    return user # returns the users input for every time the code runs


def run_game(file_name):
    
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: ' +word)


if __name__ == "__main__":
    run_game('short_words.txt')

