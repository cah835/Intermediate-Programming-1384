#Corey Henry & Aaron Shepard                 #Date Assigned:  7 apr 15
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: 14 apr 15
#File name: Lab 
#
#Program description- creates a class that runs the driver for linked lists

#Importing from the ListNode class
from ListNode import *

class LinkedList():

    #Constructs a pointer for the linked list
    def __init__(self):
        self.head = None
        
    #Inserts an item at the front of the linked list
    def insert_front(self,item):
        
 # if node is empty adds item       
        if self.head == None:
            self.head = ListNode(item)

        #adds item when the list isnt empty
        else:
            temp = ListNode(item)
            temp.set_link(self.head)
            self.head = temp
            temp = None

    #Inserts an item in a particular position of the linked list
    def insert_position(self, item, position):

        #Determines if node is empty
        if self.head == None:
            self.head = ListNode(item)

       # inserts the item if the position is at 0    
        
        else:            
            current = self.head
            if position == 0:
                temp= ListNode(item)
                temp.set_link(self.head)
                self.head= temp
                temp = None
            else:
                
 #inserts the item if the postion is great than 0               
                for each in range(position):
                    previous = current
                    current = current.get_link()
                temp = ListNode(item, current)
                previous.set_link(temp)
            
            
#inserts an item at the end of the list
    def insert_end(self, item):

    #if the list is empty it add the item to the list
        if self.head == None:
            self.head = ListNode(item)

    # adds item to the list when the list is not empty
        else:
            current = self.head
            temp = ListNode(item)

            while current.get_link() != None:
                current = current.get_link()
            current.set_link(temp)

#deletes the item at the front of the list
    def delete_front(self):
        current = self.head
        self.head = current.get_link()

#deletes the item at the end of the list
    def delete_end(self):
        current = self.head

    
        while current.get_link() != None:
            previous = current
            current = current.get_link()

        previous.set_link(None)
        
#deletes an item at a particular position in the list
    def delete_item(self,item):
        current = self.head

    #if the pointer is equal to item the item is deleted
        if current.get_item() == item:
            self.head = self.head.get_link()

    #goes through the list until current is equal to item
        else:
            while current.get_item() != item:
                previous = current
                current = current.get_link()
            previous.set_link(current.get_link())
    
# delete the whole list
    def delete_list(self):
        self.head = None

#return string version of the list allowed for None and for elements
    def __str__(self):
        if self.head == None:
            string = 'None'
            return string
        else:
            string = ''
            current = self.head
            while current != None:
                temp = current.get_item()
                string += str(temp)
                current = current.get_link()
                if current != None:
                    string += ', '
                else:
                    string += ''
            return string
