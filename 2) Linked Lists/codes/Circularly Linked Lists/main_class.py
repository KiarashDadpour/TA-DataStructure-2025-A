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
        while True:
            print(current.get_info(), end="  ")
            current = current.next
            if current == self.head:
                break

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
        return None\

    def insert_head(self, new: Node):
        if self.is_empty():
            self.head = new
            self.tail = new
            new.next = self.head  
        else:
            new.next = self.head
            self.head = new
            self.tail.next = self.head
