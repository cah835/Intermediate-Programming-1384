#Corey Henry                                 #Date Assigned: 
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: 
#File name: Lab 
#
#Program description-  

def main():
    my_list = [5,10,-5,-10,0]
    maximum = recursive_max(my_list)
    print(maximum)

def recursive_max(my_list):
    if len(my_list) == 1:
        return my_list[0]
    else:
        biggest = recursive_max(my_list[1:])
        if biggest > my_list[0]:
            return biggest
        else:
            return my_list[0]
    
main()
        
        
    
        
