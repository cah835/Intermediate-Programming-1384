#Corey Henry & natalie morrision                                #Date Assigned: 24Feb14
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: 03Mar14
#File name: Lab 
#
#Program description-  

import random
import time

##function that will take the two numbers in a list side by side and determine which is smaller
#then will put the smallest infront

def bubbleSort(aList):
    n = len(aList)
    for each in range(n):
        index =0
        for each in range(n-1):
            
            # determines which number is smaller and puts it first, then moves up one index
            
            if aList[index] > aList[index+1]:
                var1 = aList[index]
                var2 = aList[index+1]
                aList[index] = var2
                aList[index+1] = var1
                index +=1

                
            else:
                index +=1
    return



        
# function that will sort by checking the whole list for the lowest value
#and placing it first, then continuing on and on. help from interactivepython.org
def selectionSort(aList):
    for each in range(len(aList)-1,0,-1):
        mini = 0
        for index in range(1,each+1):
            if aList[index] > aList[mini]:
                mini = index
        var1 = aList[each]
        aList[each] = aList[mini]
        aList[mini] = var1

    
   

def main():
    #Create a list of 1000 random numbers
    myList = []

    for i in range(10000):
        x = random.randint(1, 25)
        myList.append(x)


    #Sort using python sort method
    start = time.time()
    myList.sort()
    stop = time.time()
    total_time = stop - start
    #print("Sorted:", myList)

    print("Time needed for python sort method: ", total_time)

    #Recreate an unordered list
    for i in range(len(myList)):
        myList[i] = random.randint(1, 25)

    #Sort using bubble sort method
    start = time.time()
    bubbleSort(myList)
    stop = time.time()
    total_time = stop - start
    #print("Sorted:", myList)

    print("Time needed for bubble sort function: ", total_time)


    #Recreate an unordered list
    for i in range(len(myList)):
        myList[i] = random.randint(1, 25)

    #Sort using selection sort method
    start = time.time()
    selectionSort(myList)
    stop = time.time()
    total_time = stop - start


    #print("Sorted:", myList)

    print("Time needed for selection sort function: ", total_time)


    input("\nPress Enter to close")

main()
