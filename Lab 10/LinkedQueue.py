#Corey Henry & Aaron Shepard                 #Date Assigned:  14 apr 15
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: 21 apr 15
#File name: Lab 
#
#Program description- creates a class for queues and linked lists

from ListNode import *
        
class LinkedQueue():
    def __init__(self):
        self.front = None
        self.rear = None

#creates a new list if empty, and adds item if the list has items
#updates rear
    def enqueue(self,item):
        if self.front == None:
            self.front = ListNode(item)
            self.rear = self.front
        else:
            temp = ListNode(item)
            current = self.rear
            self.rear = temp
            current.set_link(temp)
            
#remove first item in list and returns it
    def dequeue(self):
        current = self.front
        item = current.get_item()
        self.front = self.front.get_link()
        return item

    
#check to see if empty
    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False
#always false
    def is_full(self):
        return False

#reset to none
    def destroy(self):
        self.front = None
        self.rear = None

        
#string version of the linked lsit
    def __str__(self):
        if self.front == None:
            string = 'None'
            return string
        else:
            string = ''
            current = self.front
            while current != None:
                temp = current.get_item()
                string += str(temp)
                current = current.get_link()
                if current != None:
                    string += ', '
                else:
                    string += ''
            return string
