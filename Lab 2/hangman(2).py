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
