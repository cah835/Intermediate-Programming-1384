#Corey Henry & Natalie Morrison              #Date Assigned: 17Feb15
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: 24 Feb 15
#File name: Theater.py
#
#Program description- creates a theater seat selling systen 


#Initialize row and seat to default of 1 and create a intial 2D list
class Theater():
    def __init__(self,row =1,seat= 1):
        self.row = row
        self.seat = seat
        self.size = []
        for each in range(row):
            self.size +=[['-']* seat]


#Create a 2D list that overrides the old list
    def set_size(self, row, seat):
        self.row = row
        self.seat = seat
        self.size = []
        for each in range(row):
            self.size += [['-']* seat]


#This function takes the row and seat and replaces the '-' with '#' if open
    def sell_seat(self,row,seat):
        row_number = row -1
        seat_number = seat -1

        #if seat is not available, return false
        if self.size[row_number][seat_number] == '#':
            return(False)

        #seat is sold, return true
        else:
            self.size[row_number][seat_number] = '#'
            return(True)


#function that returns the grid to print
    def __str__(self):

        #create a empty string to return
        new = ''

        #double loop to take the index of the row and seat and add it to the string
        for row in self.size:
            for seat in row:
                new += seat
            new += '\n'
        return new
            
