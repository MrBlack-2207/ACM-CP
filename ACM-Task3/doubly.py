class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insertion at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Insertion at a specific position
    def insert_at_position(self, data, position):
        if position <= 0:
            print("Position should be >= 1")
            return
        new_node = Node(data)
        if position == 1:  # Insert at beginning
            self.insert_at_beginning(data)
            return

        temp = self.head
        for i in range(1, position-1):
            if temp is None:
                print("Position is out of bounds")
                return
            temp = temp.next

        if temp is None:
            print("Position is out of bounds")
            return

        new_node.next = temp.next
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp

    # Deletion from the beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    # Deletion from the end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None

    # Deletion from a specific position
    def delete_from_position(self, position):
        if position <= 0:
            print("Position should be >= 1")
            return
        if self.head is None:
            print("List is empty")
            return
        if position == 1:  # Deleting the head node
            self.delete_from_beginning()
            return
        temp = self.head
        for i in range(1, position):
            if temp is None:
                print("Position is out of bounds")
                return
            temp = temp.next

        if temp is None or temp.prev is None:
            print("Position is out of bounds")
            return

        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    # Traversal forward
    def traverse_forward(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # Traversal backward
    def traverse_backward(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()
