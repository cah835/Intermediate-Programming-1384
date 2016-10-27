#Corey Henry                                 #Date Assigned: 03Feb15
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: 10Feb15
#File name: Lab 3
#
#Program description-  Create a turtle the walks around and draws.



class Turtle:
    def __init__(self, grid_number):
        self.grid_number = grid_number
#create the grid using lists.
        self.grid = []
        for each in range(grid_number):
            self.grid += [['.']* grid_number]
                   
            
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
            self.grid[self.row][self.column] = '*'
            

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
                for each in range(ammount):
                    self.grid[self.row][self.column] = '*'
                    self.column += 1
                    if self.column >= self.grid_number:
                        break
            if self.direction == 2:
                for each in range(ammount):
                    self.grid[self.row][self.column] = '*'
                    self.row += 1
                    if self.row >= self.grid_number:
                        break
            if self.direction == 3:
                for each in range(ammount):
                    self.grid[self.row][self.column] = '*'
                    self.column -= 1
                    if self.column <= 0:
                        break
            if self.direction == 0:
                for each in range(ammount):
                    self.grid[self.row][self.column] = '*'
                    self.row -= 1
                    if self.column <= 0:
                        break
                    
                
            
            
        else:
            if self.direction == 1:
                for each in range(ammount):
                    self.column += 1
                    if self.column >= self.grid_number:
                        break
            if self.direction == 2:
                for each in range(ammount):
                    self.row += 1
                    if self.row >= self.grid_number:
                        break
            if self.direction == 3:
                for each in range(ammount):
                    self.column -= 1
                    if self.column <= 0:
                        break
                
            if self.direction == 0:
                for each in range(ammount):
                    self.row -= 1
                    if self.row <= 0:
                        break
                
            

    def print_grid(self):
        for row in self.grid:
            for column in row:
                print(column, end=' ')
            print(end='\n')
               
           
            
            
            
            
            
                
                
              
                
            
