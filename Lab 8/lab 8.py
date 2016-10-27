#Corey Henry & Aaron Shepard                 #Date Assigned:  17 mar 15
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: 7 apr 15
#File name: Lab 
#
#Program description- takes a creates a stack and does basic math interpitations

from Stack import*

#creates main and gets file name and adds.txt if needed
def main():
    file_name = input("Please enter the file you wish to open. ")
    if not file_name.endswith(' .txt'):
        file_name += '.txt'
        
#opens the file, creates a object called my_stack
        
    file = open(file_name)
    my_stack = Stack()

#loops to split the file into lines the splits them up
    
    for each_line in file:
        each_term = each_line.strip()
        lists = each_term.split()
        flag = False
        for each in lists:
            
 #if statement for addition
            
            if each == '+':
                if my_stack.is_empty() == False:
                    x= my_stack.pop()
                    if my_stack.is_empty() == False:
                        y= my_stack.pop()
                        value = x+y
                        my_stack.push(value)

                        #invalid statement
                if my_stack.is_empty()== True:
                    print('ERROR: ', each_term , ' is an invalid postfix expression')
                    flag = True
                    print('\n')
                    break

#if statement for minus
            elif each == '-':
                if my_stack.is_empty() == False:
                    x= my_stack.pop()
                    if my_stack.is_empty() == False:
                        y= my_stack.pop()
                        value = y-x
                        my_stack.push(value)

                        #invalid statement
                if my_stack.is_empty()== True:
                    print('ERROR: ', each_term, ' is an invalid postfix expression')
                    flag = True
                    print('\n')
                    break

#if statement for multiplication
                
            elif each == '*':
                if my_stack.is_empty() == False:
                    x= my_stack.pop()
                    if my_stack.is_empty() == False:
                        y= my_stack.pop()
                        value = x*y
                        my_stack.push(value)

                        #invalid statement
                if my_stack.is_empty()== True:
                    print('ERROR: ', each_term, ' is an invalid postfix expression')
                    flag = True
                    print('\n')
                    break

#if statement for division
                
            elif each == '/':
                if my_stack.is_empty() == False:
                    x= my_stack.pop()
                    if my_stack.is_empty() == False:
                        y= my_stack.pop()
                        value = y/x
                        my_stack.push(value)

                        #invalid statement
                if my_stack.is_empty()== True:
                    print('ERROR: ', each_term , ' is an invalid postfix expression')
                    flag = True
                    print('\n')
                    break
            else:
                try:
                    my_stack.push(int(each))
                except ValueError as err:
                    print('ERROR: ', each_term , ' is an invalid postfix expression')
                    flag = True
                    print('\n')
                    break

#conditions for printing out the strings
        if flag == False:
            x= my_stack.pop()
            if my_stack.is_empty() == True:
                print('Expresssion: ',str(each_term))
                print('Answer = ',x)
                print('\n')
            else:
                print('ERROR: ' ,each_term , 'is an invalid postfix expression')
                print('\n')
        
main()



        
        
    
    
    
