from DoublyLinkedList import *
from ListNode2 import *

def main():
    grade = 0

    #1 Tests init
    myList = DoublyLinkedList()
    grade += 5
    print("Grade after test  1: ", grade)

    #2 Tests adding to an empty list and __str__
    myList.in_order_insert(10)
    if str(myList) == "10":
        grade += 10
    print("Grade after test  2: ", grade)

    #3 Tests __str__
    if str(myList) == "10":
        grade += 5
    print("Grade after test  3: ", grade)

    #4 Tests adding to the beginning
    myList.in_order_insert(5)
    if str(myList) == "5, 10":
        grade += 10
    print("Grade after test  4: ", grade)
    print(str(myList))

    #5 Tests adding to the end
    myList.in_order_insert(20)
    if str(myList) == "5, 10, 20":
        grade += 10
    print("Grade after test  5: ", grade)
    print(str(myList))

    #6 Tests insert in the middle
    myList.in_order_insert(15)
    if str(myList) == "5, 10, 15, 20":
        grade += 10
    print("Grade after test  6: ", grade)
    print(str(myList))

    #7 Tests __len__
    if len(myList) == 4:
        grade += 5
    print("Grade after test  7: ", grade)
    print(str(myList))

    #8 Tests delete_item when item isn't there
    try:
        myList.delete_item(0)
    except ValueError as ex:
        if str(ex) == "This item is not in the list":
            grade += 5
    print("Grade after test  8: ", grade)

    #9 Tests delete_item n list is empty
    newList = DoublyLinkedList()
    try:
        newList.delete_item(0)
    except ValueError as ex:
        if str(ex) == "This item is not in the list":
            grade += 10
    print("Grade after test  9: ", grade)

    #10 Tests delete_item when item is there
    myList.delete_item(10)
    if str(myList) == "5, 15, 20":
        grade += 10
    print("Grade after test 10: ", grade)

    #11 Tests total_list
    newList = DoublyLinkedList()
    for each in range(65, 100):
        newList.in_order_insert(each)
    total = newList.total_list()
    other_total = 0
    for each in range(65, 100):
        other_total += each
    if total == other_total:
        grade += 10
    print("Grade after test 11: ", grade)

    #12 Tests get_first
    first = newList.get_first()
    if first == 65:
        grade += 5
    print("Grade after test 12: ", grade)

    #13 Tests get_last
    last = newList.get_last()
    if last == 99:
        grade += 5
    print("Grade after test 13: ", grade)

    
    
    
    return

main()
