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
