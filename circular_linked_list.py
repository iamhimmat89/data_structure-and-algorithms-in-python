print("\nWelcome to Circular Linked List Data Structure.!!!\n")

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


# Class CircularLinkedList: Used for different operation insert, delete, display, search etc.
class CircularLinkedList:

    # constructor
    def __init__(self):
        self.head = None
        self.length = 0

    # Method to insert a node at the beginning of the list
    def insert(self, data):
        new_node = Node()
        new_node.set_data(data)

        if self.length == 0:
            self.head = new_node
            new_node.set_next(new_node)
        else:
            current = self.head

            while current.get_next() != self.head:
                current = current.get_next()

            new_node.set_next(self.head)
            current.set_next(new_node)

        self.length += 1
        print(str(data) + " is successfully inserted in the list")

    # Method to delete a node from the beginning of the list
    def delete(self):
        if self.length == 0:
            print("List is empty\n")
        else:
            previous = self.head
            current = self.head

            while current.get_next() != self.head:
                previous = current
                current = current.get_next()

            previous.set_next(current.get_next())
            self.length -= 1
            print("Node is deleted from the list")

    # Method to delete a node as per given value of the list
    def delete_value(self, value):
        if self.length == 0:
            print("List is empty\n")
        else:
            current = self.head
            previous = self.head

            while current.get_next() != self.head or current.get_data() != value:
                if current.data == value:
                    previous.set_next(current.get_next())
                    self.length -= 1
                    print(str(value) + " is deleted from the list")
                    return
                else:
                    previous = current
                    current = current.get_next()

            if current.get_next() == self.head and current.get_data() == value:
                previous.set_next(current.get_next())
            else:
                print(str(value) + " is not present in the list")

    # Method to search (using iterative) a node from the list
    def search(self, data):
        if self.length == 0:
            print("List is empty\n")
        else:
            count = 0
            current = self.head

            while current.get_next() != self.head:
                if current.data == data:
                    print(str(data) + " is present at index " + str(count) + " in the list\n")
                    return
                current = current.get_next()
                count += 1
            if current.data == data:
                print(str(data) + " is present at index " + str(count) + " in the list\n")
            else:
                print(str(data) + " is not present in the list\n")

    # Method to display the list
    def display(self):
        if self.length == 0:
            print("List is empty\n")
        else:
            print("Linked List: ")
            current = self.head

            while current.get_next() != self.head:
                print(str(current.data))
                current = current.get_next()

            print(current.data)

    # Method to clear the list
    def clear(self):
        if self.length == 0:
            print("List is empty\n")
        else:
            self.head = None
            print("Removed all node from the list.")


linkedlist = CircularLinkedList()

while True:
    print("Please enter Choice: ")
    print("1. Insert node to list")
    print("2. Delete node from list")
    print("3. Display list")
    print("4. Search node in list")
    print("5. Clear list")
    print("6. Exit")
    print("")
    print("input: ")
    choice = int(input())

    if choice == 1:
        print("Please enter data to be insert: ")
        insert_data = int(input())

        linkedlist.insert(insert_data)
    elif choice == 2:
        print("1. Delete node from the list")
        print("2. Node value to be delete from the list")
        print("")
        print("Deletion choice: ")
        delete_choice = int(input())

        if delete_choice == 1:
            linkedlist.delete()
        elif delete_choice == 2:
            print("Please enter value to be delete from the list: ")
            delete_data = int(input())
            linkedlist.delete_value(delete_data)
        else:
            print("Please enter valid input")
    elif choice == 3:
        linkedlist.display()
    elif choice == 4:
        print("Please enter value to search in the list: ")
        search_data = int(input())
        linkedlist.search(search_data)
    elif choice == 5:
        linkedlist.clear()
    elif choice == 6:
        print("Good Bye..!!!")
        break
    else:
        print("Please enter valid input")
