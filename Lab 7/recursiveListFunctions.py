#Corey Henry & Aaron Shepard                 #Date Assigned:  17 mar 15
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: 24 mar 15
#File name: Lab 
#
#Program description- recursice functions for max,min, print, quicksort. 

# function that will take the list and find the maxiumum value out of the list
# and returns the highest

def recursive_max(my_list):
    if len(my_list) == 1:
        return my_list[0]
    else:
        biggest = recursive_max(my_list[1:])
        if biggest > my_list[0]:
            return biggest
        else:
            return my_list[0]

# takes the first index of the list and adds the rest of the list onto the first index
# uses recursice to keep adding the numbers
def recursive_sum(my_list):
    if len(my_list) == 1:
        return my_list[0]
    else:
        return my_list[0] + recursive_sum(my_list[1:])
    
        
    
# uses the same function as the min you just switch the signs, finds the lowest
# value in the list and returns it.
def recursive_min(my_list):
    if len(my_list) ==1:
        return my_list[0]
    else:
        smallest = recursive_min(my_list[1:])
        if smallest < my_list[0]:
            return smallest
        else:
            return my_list[0]

#prints the list starting with the first index and goes through, when it reaches
# it will print the last index in the list        
def recursive_print(my_list):
    if len(my_list) == 1:
        print(my_list[0])
    else:
        print(my_list[0], end = ' ')
        recursive_print(my_list[1:])
    
#taken from class slides. takes the middle number and splits the list in two.
def quicksort(my_list, first, last):
    if first < last - 1:
        pivot = median3(my_list, first, last)
        i = first
        j = last -1

        while True:
            i+=1
            while my_list[i] < pivot:
                i +=1
            j -= 1
            while my_list[j] > pivot:
                j -=1
            if i < j:
                my_list[i], my_list[j], = my_list[j], my_list[i]
            else:
                break

        my_list[i], my_list[last - 1] = my_list[last -1], my_list[i]
        quicksort(my_list, first, i -1)
        quicksort(my_list, i+1, last)

    elif first < last:
        if my_list[first] > my_list[last]:
            my_list[first], my_list[last] = my_list[last], my_list[first]

def median3(my_list, first, last):
    center = (first + last) //2
    if my_list[center] < my_list[first]:
        my_list[first], my_list[center] = my_list[center], my_list[first]
    if my_list[last] < my_list[first]:
        my_list[first], my_list[last] = my_list[last], my_list[first]
    if my_list[last] < my_list[center]:
        my_list[center], my_list[last] = my_list[last], my_list[center]
    my_list[center], my_list[last -1] = my_list[last-1], my_list[center]
    return my_list[last-1]
                            
    
        
        
    
        
