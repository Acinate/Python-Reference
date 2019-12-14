# Node
class Node:

    # Function to initialize the Node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class
class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None

    # Function to print contents of a Linked List
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    # Start with the empty list
    list = LinkedList()

    list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Link first node with second
    list.head.next = second

    # Link second node with third
    second.next = third

    list.print_list()
