#Corey Henry                                 #Date Assigned: 05Nov14
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: Jan 27
#File name: Lab1-protected files
#
#Program description- create and/or open a file that is password protected.


#create a function that will create a file
def create_file():
#determine password and check to see if the equal each other
    password = input('Please enter the password for the file you wish to create: ')
    re_pass = input('Please Re-enter the pass word for the file you wish to create: ')
    while password != re_pass:
        print('Passwords do not match please try again')
        password = input('Please enter the password for the file you wish to create: ')
        re_pass = input('Please Re-enter the pass word for the file you wish to create: ')
    file_name = input('Please enter the name of the file you wish to create: ')
#add .txt to the file
    if not file_name.endswith('.txt'):
        file_name += '.txt'
#open file and pass the password and any information they want too and set it up to cancel when they enter :wq
#dont add :wq to the file
    infile = open(file_name, 'w')
    infile.write(password)
    information = '\n'
    while information != ':wq':
        information = input('Please enter the information you wish to add to the file: ')
        infile.write('\n')
        if information != ':wq':
            infile.write(information)
    infile.close()
    
    
#function to open the file and read the password.   
def open_file():
    infile = input('what is the file name you wish to open? ')
    if not infile.endswith('.txt'):
        infile += ('.txt')
    count = 1
    infile = open(infile, 'r')
    password = infile.readline()
    password= password.strip('\n')
    information= infile.read()
    infile.close()
    prompt = 'wrong'
#while loop to give 3 chances to get password correct and print the information
    while prompt != password and count < 4:
        prompt = input('Please enter the password to open the file: ')
        count +=1
        
    if prompt == password:
        print(information)
        

    else:
        return

#main function to give them the option of opening or creating the file
def main():
    option = input('Would you like to open or create a file(type stop to end program)? ')
    if option == 'open':
        open_file()
        main()
    if option == 'create':
        create_file()
        main()
    else:
        quit
# run main 
main()
        
