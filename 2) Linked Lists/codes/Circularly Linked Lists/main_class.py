class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def traversal(self):
        if self.is_empty():
            return "Empty List!!!"
        current = self.head
        while current:
            print(current.get_info(),end="  ")
            if current.next == self.head:
                return
            current = current.next 
        print()
            

    def search_node(self, value):
        if self.is_empty():
            return "Empty List!!!"
        current = self.head
        while True:
            if current.info == value:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def insert_head(self, new: Node):
        if self.is_empty():
            self.head = new
            self.tail = new
            new.next = self.head  
        else:
            new.next = self.head
            self.head = new
            self.tail.next = self.head

    def insert_tail(self, new: Node):
        if self.is_empty():
            self.head = new
            self.tail = new
            new.next = self.head  
        else:
            self.tail.next = new
            self.tail = new
            self.tail.next = self.head

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
        elif self.head == self.tail: 
            self.head = self.tail = None
        else:
            current = self.head 
            self.head = self.head.next
            self.tail.next = self.head.get_next()
            current.next = None
            return

