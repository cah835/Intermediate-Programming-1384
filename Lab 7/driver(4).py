from recursiveListFunctions import *
import random 

def main():
    my_list = []
    for each in range(10):
        my_list.append(random.randint(0, 100))

    print("My list:", end = ' ')
    recursive_print(my_list)
    print()
    
    total = recursive_sum(my_list)
    print("Sum of list items: ", total, '\n')

    minimum = recursive_min(my_list)
    print("Minimum of list items: ", minimum, '\n')

    maximum = recursive_max(my_list)
    print("Maximum of list items: ", maximum, '\n')

    quicksort(my_list, 0, len(my_list) - 1)
    print("My sorted list: ", end = ' ')
    recursive_print(my_list)

main()
