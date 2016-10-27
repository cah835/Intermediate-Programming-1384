#Corey Henry                                 #Date Assigned: 
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: 
#File name: Lab 
#
#Program description-

class ListNode(object):
    def __init__(self, item = None, link = None):

        self.__item = item

        self.__link = link
        return

    def set_item(self, item):
        self.__item = item
        return

    def get_item(self):
        return(self.__item)

    def set_link(self,link):
        self.__link = link
        return

    def get_link(self):
        return(self.__link)


def main():
    #start the linked list head
    head = ListNode(3)
    #insert a new node containing 5 at the beggining
    #create new node
    temp = ListNode(5)
    #store address of the old first node in our new node
    temp.set_link(head)
    #make hold the address of the new first node
    head = temp
    #house keeping
    temp = None

    # OR...

    temp = ListNode(7,head)
    head = temp
    temp = None

    #OR
    head = ListNode(9,head)

    #traverse the list
    #start at the beggining of the list
    temp = head
    #loop until none is found
    while temp != None:
        print(temp.get_item())
        #move to the next node
        temp = temp.get_link()
        

    
    print('\n')
    current = head
    while current.get_item() != 7:
        current = current.get_link()

    temp = ListNode(5,current.get_link())

    current.set_link(temp)
    
    temp = head
    #loop until none is found
    while temp != None:
        print(temp.get_item())
        #move to the next node
        temp = temp.get_link()

    print('\n')

    #inserting at the end
    current = head
    temp = ListNode(4)

    while current.get_link() != None:
        current = current.get_link()
        
    current.set_link(temp)


    #previous and current links

    current = head

    while current.get_item() != 5:
        previous = current
        current = current.get_link()

    previous.set_link(current.get_link())

    #start at the beggining of the list
    temp = head
    #loop until none is found
    while temp != None:
        print(temp.get_item())
        #move to the next node
        temp = temp.get_link()

    print('\n')

    # deleting the last node
    current = head

    while current.get_link() != None:
        previous = current
        current = current.get_link()

    previous.set_link(None)


     #start at the beggining of the list
    temp = head
    #loop until none is found
    while temp != None:
        print(temp.get_item())
        #move to the next node
        temp = temp.get_link()


    return
        

main()
    
        

        
    
        
