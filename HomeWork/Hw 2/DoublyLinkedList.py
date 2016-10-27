#Corey Henry                                 #Date Assigned: 14 APR 15
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: 21 APR 15
#File name: homework 2
#
#Program description- creates a double linked list and functions to go through a driver

from ListNode2 import *

class DoublyLinkedList():

#initalizes the head and the rear    
    def __init__(self):
        self.head = None
        self.rear = None
        return

#counts the items in the list by adding 1 to count each time you traverse the list
    def __len__(self):
        count = 0
        if self.head == None:
            return 0
        else:
            current = self.head
            while current != None:
                count += 1
                current = current.get_next()
            return count

#turns the list into a strin
    def __str__(self):
        if self.head == None:
            string = "None"
            return string
        else:
            
#creates a empty string and adds the items to the string and a , if its not the last node
            string = ""
            current = self.head
            while current != None:
                temp = current.get_item()
                string += str(temp)
                current = current.get_next()
                if current != None:
                    string += ", "
                else:
                    string += ""
            return string

#adds the items to the list
    def in_order_insert(self,item):
        flag = True
        temp = ListNode2(item)
        current = self.head

#condition if the list is empty
        if self.head == None:
            self.head = temp

#condition if the first item is greater than the item you are adding
        elif current.get_item() > item:
            self.head = temp
            temp.set_next(current)
            current.set_previous(temp)
            
#traveres list to find where the item will go in the list
        else:
            while current != None and current.get_item() < item:
                previous = current
                current = current.get_next()
                
#condition for if the item you are adding is the largest in the list
            if current == None:
                temp.set_previous(previous)
                previous.set_next(temp)
                temp.set_next(None)
                #set flag to false so you dont try to double set links
                flag = False
                
#adds the item to the list and changes all the arrows                
            if flag == True:
                temp.set_previous(previous)
                previous.set_next(temp)
                temp.set_next(current)
                current.set_previous(temp)
            
# deletes an item in the list
    def delete_item(self,item):
        current = self.head
        flag = False
        
#condition if you try to delete from an empty list
        if self.head == None:
            raise ValueError("This item is not in the list")

#condidtion if the first item is what you are trying to delete
        elif current.get_item() == item:
            self.head = current.get_next()

#traverse the list and set flag to true if the item exsists in the list            
        else:
            while current != None and current.get_item() != item:
                previous = current
                current = current.get_next()
                if current != None and current.get_item() == item:
                    flag = True
                    
#if the item exsists then get rid of it                
            if flag == True:
                if current.get_next() != None:
                    current = current.get_next()
                current.set_previous(previous)
                previous.set_next(current)
                
#if the item doesnt not exsist raise value error
            else:
                raise ValueError("This item is not in the list")
                 
            
        
        
#create a function that adds up the numbers in the list
    def total_list(self):
        current = self.head
        total = 0
        while current != None:
            number = current.get_item()
            total += number
            current = current.get_next()
        return total

#returns the first item in the list
    def get_first(self):
        current = self.head
        return(current.get_item())

#returns the last item in the list
    def get_last(self):
        current = self.head
        while current != None:
            previous = current
            current = current.get_next()
        return(previous.get_item())
        


        
