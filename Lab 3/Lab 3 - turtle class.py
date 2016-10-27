#Corey Henry                                 #Date Assigned: 03Feb15
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: 10Feb15
#File name: Lab 3
#
#Program description-  Create a turtle the walks around and draws.



class Turtle:
    def __init__(self, grid_number):
#create the grid using lists.
        self.grid = [['.']* grid_number]* grid_number
                   
            
#set the direction starting point           
        self.direction = 1
#set the startion location, use  and y's for location for rows and collumns
        self.row = 0
        self.column = 0

        return
        
        
        

    def change_pen_position(self,command):
        if command == 1:
            self.pen_position = 'up'
        

        if command == 2:
            self.pen_position = 'down'
            self.grid[row][column] = '*'
            

    def turn_right(self):
        self.direction += 1
        if self.direction == 4:
            self.direction = 0

    def turn_left(self):
        self.direction -= 1
        if self.direction == -1:
            self.direction = 3

    def move_forward(self, ammount):
        if self.pen_position is 'down':
            if self.direction == 1:
                for each in range(ammount)
                    self.grid[row][column] = '*'
                    slef.column += 1
            if self.direction == 2:
                for each in range(ammount)
                    self.grid[row][column] = '*'
                    self.row[index] += ammount
            if self.direction == 3:
                for each in range(ammount)
                    self.grid[row][column] = '*'
                    self.row[index] -= 1
            if self.direction == 0:
                for each in range(ammount)
                    self.grid[row][column] = '*'
                    self.rows[index] -= 1
                
            
            
        else:
            if direction == 1:
                self.column[index] += ammount
            if direction == 2:
                self.row[index] += ammount
            if direction == 3:
                self.row[index] -= 1
            if direction == 0:
                self.rows[index] -= 1
            

    def print_grid(self,grid):
       index = 0
       for each in range(grid_number):
          print(grid[index])
          index += 1
