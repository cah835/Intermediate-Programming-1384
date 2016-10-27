from Turtle import *

def main():
    #Create turtle using a size 20 grid for the turtle to walk in
    my_turtle = Turtle(20)

    #Get the file name that contains turtle instructions from the user and open
    #the file for reading
    file_name = input("Enter the file containing the turtle's instructions: ")

    #If the file_name doesn't end with .txt, then add it
    if not file_name.endswith(".txt"):
        file_name += '.txt'

    #Loop until the user types in a valid file name
    file_exists = False
    while not file_exists:
        try:
            instructions = open(file_name)
        except FileNotFoundError as er:
            #Print error message and get another file name to try.
            print("That file does not exist")
            file_name = input("Please re-enter the file name: ")

            #Add .txt if not at the end of the file name
            if not file_name.endswith(".txt"):
                file_name += '.txt'
        else:
            #If the file opened, change flag so that the loop ends
            file_exists = True

    #Read the file, one line at a time
    for each_line in instructions:
        #Change pen position to up
        if each_line[0] == '1':
            my_turtle.change_pen_position(1)

        #Change pen position to down
        elif each_line[0] == '2':
            my_turtle.change_pen_position(2)

        #Turtle turns to the right
        elif each_line[0] == '3':
            my_turtle.turn_right()

        #Turtle turns to the left
        elif each_line[0] == '4':
            my_turtle.turn_left()

        #Turtle moves forward in the direction it is facing
        #If the pen is down, a line is drawn
        elif each_line[0] == '5':
            command = each_line.split()
            my_turtle.move_forward(int(command[1]))

        #Print the grid
        elif each_line[0] == '6':
            my_turtle.print_grid()

        #Print thank you message and end the program
        elif each_line[0] == '9':
            print("Thanks for drawing with us.")
            return
       
        

    
    #Close the file
    instructions.close()


main()
