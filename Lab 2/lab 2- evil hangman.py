#Corey Henry                                 #Date Assigned: 27jan15
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: Feb 3
#File name: Lab2-Evil Hangman
#
#Program description- create a game of evil hangman

#create main function to run program
def main():
    #get the number of letters
    number_of_letters = int(input('Welcome to Hangman, please choose the number of letters you wish to play with: '))
#set object
    display = Hangman()
#set guesses to 0
    guesses = 0
#create empty list for the wrong letters
    wrong_letters = []
#create the base that will show all the letters
    base = []
    letters = Word(number_of_letters)
#loop that creates the ammount of spaces for the ammount of letters chosen   
    for each in range(number_of_letters):
        base.append('_ ')
#loop for the ammounnt of guesses you are allowed
    while guesses <= 7:
        cheat = letters.get_word()
#option to choose word or letter guess
        guess = input('Would you like to guess a letter or the word? ')
#if statements that split the difference between letter or word guesses
        if guess == 'letter':
            letter = input('What is the letter you would like to guess? ')
            returned_value = letters.guess_letter(letter)
#if the letter is not in the word, add to the guess count and add to the list of wrong letters and print the wrong letters.
            if returned_value[0] == -1:
                display.guessed_wrong()
                wrong_letters.append(letter)
                print(wrong_letters)
                guesses += 1
                    
                    
            else:
                for each_index in returned_value:
                    base[each_index]=(letter)
                    win =''
#create a loop to make a string format of the list base
                    for each_index in base:
                        win += (each_index)
#use the win and cheat to determine if you win the game
                    if win == cheat:
                        print('Congrats you win!')
                        quit()
            print(base)
            display.print_hangman()
        if guess == 'word':
            word = input('What word do you think it is? ')
            returned_answer = letters.guess_word(word)
        if guesses == 7:
            cheat = letters.get_word()
            print('Sorry you lose, the word was ',cheat)
            quit()

        

class Hangman:
    #Builds the gallows
    def __init__(self):
        self.gallows = [[' ', ' ', '_', '_', '_', ' '],
           [' ', '|', ' ', ' ', '|', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           ['_', '|', '_', ' ', ' ', ' ']]

        self.guesses = 0

    #Increments the number of incorrect guesses
    def guessed_wrong(self):
        self.guesses += 1

        if self.guesses > 8:
            raise ValueError("The man has been hung.  No more guesses are allowed")

    #Prints the hangman
    def print_hangman(self):
        #Update the gallows
        if self.guesses >= 1:
            #Add head
            self.gallows[2][4] = 'O'
        if self.guesses >= 2:
            #Add neck
            self.gallows[3][4] = '|'
        if self.guesses >= 3:
            #Add left arm
            self.gallows[3][3] = '\\'
        if self.guesses >= 4:
            #Add right arm
            self.gallows[3][5] = '/'
        if self.guesses >= 5:
            #Add torso
            self.gallows[4][4] = '|'
        if self.guesses >= 6:
            #Add left leg
            self.gallows[5][3] = '/'
        if self.guesses >= 7:
            #Add right leg
            self.gallows[5][5] = '\\'

        #Print the hangman
        for each in self.gallows:
            one_line = ""
            for each_char in each:
                one_line += each_char
            print(one_line)

import urllib.request
import random


class Word:
    #Initializes the dictionary for all possible words of the correct lenght
    def __init__(self, number_of_letters):
        if type(number_of_letters) is not int:
            raise TypeError ("Words need a length that is an integer data type.")
        
        page = urllib.request.urlopen("http://nifty.stanford.edu/2011/schwarz-evil-hangman/dictionary.txt")
        text = page.read().decode("utf8")

        all_words = text.split()
        self.dictionary = []

        #Build dictionary
        for each in all_words:
            if len(each) == number_of_letters:
                self.dictionary.append(each)

        page.close()

        if len(self.dictionary) < 1:
            raise ValueError ("There are no words of that length in the dictionary.")
        

        #print(self.dictionary)

    #Models guessing a letter.  It requires a character.  It returns a
    #list of positions the letter in the word.  If the letter is not in the
    #word, it returns a list that contains a -1.
    def guess_letter(self, letter):
        if len(letter) > 1:
            raise ValueError ("Must send a single letter.")

        #Create an empty list to hold the positions of the letter in the word
        positions = []
        
        #Evil hangman rules
        if len(self.dictionary) > 1:
            temp = []
            #Build a list that contains all words that have the guessed letter
            for each_word in self.dictionary:
                if letter in each_word:
                    temp.append(each_word)
            #If all words with guessed letter can be removed and still have words
            #left in the list of possible words, remove them
            if len(temp) < len(self.dictionary):
                for each_word in temp:
                    self.dictionary.remove(each_word)
            #If all words in list of possibles contain guessed letter, choose a
            #word randomly
            else:
                random_position = random.randrange(len(self.dictionary))
                word = self.dictionary[random_position]
                self.dictionary = [word]
                
        
        #Regular hangman rules
        if len(self.dictionary) == 1:
            word = self.dictionary[0]
            #Record positions where the letter is found
            index = 0
            while index < len(word):
                if word[index] == letter:
                    positions.append(index)
                index += 1

        #If no letter was found
        if len(positions) == 0:
            positions.append(-1)
            
        return positions

    #Models guessing a word.  It requires a string.  It returns a either
    #a True (the guessed word is correct) or False.
    def guess_word(self, word):
        if len(self.dictionary) > 1:
            self.dictionary.remove(word)
            return False
        if word == self.dictionary[0]:
            return True
        

    #Returns the word or the first word in the list of possible words
    def get_word(self):
        return self.dictionary[0]


main()
