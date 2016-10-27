class Stack:
    def __init__(self):
        self.__the_list = []

    def push(self, item):
        self.__the_list.append(item)

    def pop(self):
        return self.__the_list.pop()

    def destroy(self):
        self.__the_list = []

    def is_empty(self):
        if len(self.__the_list) ==0:
            return True
        return False

    def is_full(self):
        return False
    
    def __str__(self):
        lists = str(self.__the_list)
        return(lists.strip('[]'))
    
        
