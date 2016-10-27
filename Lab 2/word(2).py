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
            
