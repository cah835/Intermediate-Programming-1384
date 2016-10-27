class ListNode2:
    def __init__(self, item = None, pre = None, nex = None):
        self.__item = item
        self.__previous = pre
        self.__next = nex
        return

    def get_item(self):
        return self.__item

    def get_previous(self):
        return self.__previous

    def get_next(self):
        return self.__next

    def set_item(self, item):
        self.__item = item
        return

    def set_previous(self, pre):
        self.__previous = pre
        return

    def set_next(self, nex):
        self.__next = nex
        return
    
