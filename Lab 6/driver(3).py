import random
import time

#Add sort functions here
#def bubbleSort(aList):

#def selectionSort(aList):


def main():
    #Create a list of 1000 random numbers
    myList = []

    for i in range(10000):
        x = random.randint(1, 10000)
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
        myList[i] = random.randint(1, 10000)

    #Sort using bubble sort method
    start = time.time()
    bubbleSort(myList)
    stop = time.time()
    total_time = stop - start
    #print("Sorted:", myList)

    print("Time needed for bubble sort function: ", total_time)


    #Recreate an unordered list
    for i in range(len(myList)):
        myList[i] = random.randint(1, 10000)

    #Sort using selection sort method
    start = time.time()
    selectionSort(myList)
    stop = time.time()
    total_time = stop - start

main()
    #print("Sorted:", myList)

    print("Time needed for selection sort function: ", total_time)


    input("\nPress Enter to close")
