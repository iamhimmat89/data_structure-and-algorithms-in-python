print("\nWelcome to Stack(linked-list) Data Structure.!!!\n")

# Class Node: This is representation of a single node
class Node:

    # constructor
    def __init__(self):
        self.data = None
        self.next = None

    # Method to get data of a node
    def get_data(self):
        return self.data

    # Method to set data of a node
    def set_data(self, data):
        self.data = data

    # Method to get next data of a node
    def get_next(self):
        return self.next

    # Method to set next data of a node
    def set_next(self, next):
        self.next = next


# Class Stack: Used for different operation insert, delete, display, search etc.
class Stack:

    # constructor
    def __init__(self):
        self.top = None
        self.length = 0

    # Method to insert a node at the beginning of the list
    def push(self, data):
        new_node = Node()
        new_node.set_data(data)

        if self.length == 0:
            self.top = new_node
        else:
            new_node.set_next(self.top)
            self.top = new_node

        self.length += 1
        print(str(data) + " is successfully pushed")

    # Method to delete a node from the beginning of the list
    def pop(self):
        if self.length == 0:
            print("Stack is empty\n")
        else:
            self.top = self.top.get_next()
            self.length -= 1
            print("Pop - Successful")

    # Method to display the list
    def display(self):
        if self.length == 0:
            print("Stack is empty\n")
        else:
            print("Stack (top-to-bottom): ")
            current = self.top

            while current != None:
                print(str(current.data))
                current = current.get_next()


stack1 = Stack()

while True:
    print("Please enter Choice: ")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    print("")
    print("input: ")
    choice = int(input())

    if choice == 1:
        print("Please enter value to push: ")
        insert_data = int(input())
        stack1.push(insert_data)
    elif choice == 2:
        stack1.pop()
    elif choice == 3:
        stack1.display()
    elif choice == 4:
        print("Good Bye..!!!")
        break
    else:
        print("Please enter valid input")

