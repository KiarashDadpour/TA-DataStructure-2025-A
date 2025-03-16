class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def get_size(self):
        pass 

    def is_empty(self):
        return self.head is None 

    def traversal(self):
        if self.is_empty():
            return "Empty List!!!"
        current = self.head
        while current:
            print(current.get_info(),end="  ")
            current = current.next
        
    def search_node(self, value):
        if self.is_empty():
            return "Empty List!!!"
        current = self.head
        found = False
        while (found is False) and (current is not None):
            if current.info == value:
                found = True
                return current
            else:
                current = current.next
        return current

    def insert_head(self, new: Node):
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head = new

    def insert_tail(self, new: Node):
        if self.head is None:
            self.head = new
        else:
            self.tail.next = new
            self.tail = new 

    def insert_after_node(self, new: Node, after: Node):
        if self.is_empty():
            self.head = new
        else:
            current = self.head
            while current:
                if current.info == after.info:
                    new.next = current.next
                    current.next = new
                    return True
                current = current.next 

    def delete_head(self):
        if self.is_empty():
            return "Empty List!!!"
        else:
            current = self.head 
            self.head = self.head.get_next()
            current.next = None 

