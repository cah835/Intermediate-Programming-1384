class ListNode:
    def __init__(self, item = None, link = None):
        self.__item = item
        self.__link = link

    def set_item(self, item):
        self.__item = item
        return

    def set_link(self, link):
        self.__link = link
        return

    def get_item(self):
        return self.__item

    def get_link(self):
        return self.__link
    
