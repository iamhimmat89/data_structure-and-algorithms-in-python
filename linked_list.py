print("\nWelcome to Singly Linked List Data Structure.!!!\n")


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


# Class SinglyLinkedList: Used for different operation insert, delete, display, search etc.
class SinglyLinkedList:

    # constructor
    def __init__(self):
        self.head = None
        self.length = 0

    # Method to insert a node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node()
        new_node.set_data(data)

        if self.length == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

        self.length += 1
        print(str(data) + " is successfully inserted at the beginning of the list")

    # Method to insert a node at the end of the list
    def insert_at_end(self, data):
        if self.length == 0:
            self.insert_at_beginning(data)
        else:
            new_node = Node()
            new_node.set_data(data)

            current = self.head

            while current.get_next() != None:
                current = current.get_next()

            current.set_next(new_node)
            self.length += 1
            print(str(data) + " is successfully inserted at the end of the list")

    # Method to insert a node at the given position of the list
    def insert_at_pos(self, pos, data):
        if pos > self.length or pos < 0:
            print("Position does not exist. Please enter valid position. List length is " + str(self.length))
            return
        elif pos == 0:
            self.insert_at_beginning(data)
        elif pos == self.length:
            self.insert_at_end(data)
        else:
            new_node = Node()
            new_node.set_data(data)
            count = 1
            current = self.head

            while count < pos - 1:
                current = current.get_next()
                count += 1

            new_node.set_next(current.get_next())
            current.set_next(new_node)

            self.length += 1
            print(str(data) + " is successfully inserted at the position " + str(pos) + " in the list")

    # Method to delete a node from the beginning of the list
    def delete_from_beginning(self):
        if self.length == 0:
            print("List is empty\n")
        else:
            self.head = self.head.get_next()
            self.length -= 1
            print("Node is deleted from the beginning of the list")

    # Method to delete a node from the end of the list
    def delete_from_end(self):
        if self.length == 0:
            print("List is empty\n")
        else:
            current = self.head
            previous = self.head

            while current.get_next() is not None:
                previous = current
                current = current.get_next()

            previous.set_next(None)
            self.length -= 1
            print("Node is deleted from the end of the list")

    # Method to delete a node from the given position of the list
    def delete_from_pos(self, pos):
        if self.length == 0:
            print("List is empty\n")
        elif pos == 1:
            self.delete_from_beginning()
        elif pos == self.length:
            self.delete_from_end()
        else:
            count = 0
            current = self.head
            previous = self.head

            if pos > self.length or pos < 0:
                print("Position does not exist. Please enter valid position. List length is " + str(self.length))
            else:
                while current.get_next() is not None or count < pos:
                    count = count + 1
                    if count == pos:
                        previous.set_next(current.get_next())
                        self.length -= 1
                        print("Node is deleted from position " + str(pos))
                    else:
                        previous = current
                        current = current.get_next()

    # Method to delete a node as per given value of the list
    def delete_value(self, value):
        if self.length == 0:
            print("List is empty\n")
        else:
            current = self.head
            previous = self.head

            if current.data == value:
                self.delete_from_beginning()
            else:
                while current.get_next() is not None or current.get_data() != value:
                    if current.data == value:
                        previous.set_next(current.get_next())
                        self.length -= 1
                        print(str(value) + " is deleted from the list")
                        return
                    else:
                        previous = current
                        current = current.get_next()

                if current.get_next() is None and current.get_data() == value:
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

            while current is not None:
                if current.data == data:
                    print(str(data) + " is present at index " + str(count) + " in the list\n")
                    return
                current = current.get_next()
                count += 1
            print(str(data) + " is not present in the list\n")

    # Method to search (using recursive) a node from the list
    def search_recursive(self, node, data):
        if not node:
            print(str(data) + " is not present in the list\n")
            return

        if node.data == data:
            print(str(data) + " is present in the list\n")
            return

        return self.search(node.next, data)

    # Method to display the list
    def display(self):
        if self.length == 0:
            print("List is empty\n")
        else:
            print("Linked List: ")
            current = self.head

            while current is not None:
                print(str(current.data))
                current = current.get_next()

    # Method to clear the list
    def clear(self):
        if self.length == 0:
            print("List is empty\n")
        else:
            self.head = None
            print("Removed all node from the list.")


linkedlist = SinglyLinkedList()

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
        print("1. Insert node at the beginning of the list")
        print("2. Insert node at the end of the list")
        print("3. Insert node at particular position in the list")
        print("")
        print("Inserstion choice: ")
        insert_choice = int(input())

        if insert_choice == 1:
            print("Please enter data to be insert: ")
            insert_data = int(input())

            linkedlist.insert_at_beginning(insert_data)
        elif insert_choice == 2:
            print("Please enter data to be insert: ")
            insert_data = int(input())

            linkedlist.insert_at_end(insert_data)
        elif insert_choice == 3:
            print("Please enter position: ")
            insert_data_pos = int(input())
            print("Please enter data to be insert: ")
            insert_data = int(input())

            linkedlist.insert_at_pos(insert_data_pos, insert_data)
        else:
            print("Please enter valid input")
    elif choice == 2:
        print("1. Delete node from the beginning of the list")
        print("2. Delete last node from the list")
        print("3. Delete node from particular position")
        print("4. Delete value from the list")
        print("")
        print("Deletion choice: ")
        delete_choice = int(input())

        if delete_choice == 1:
            linkedlist.delete_from_beginning()
        elif delete_choice == 2:
            linkedlist.delete_from_end()
        elif delete_choice == 3:
            print("Please enter position: ")
            delete_data_pos = int(input())
            linkedlist.delete_from_pos(delete_data_pos)
        elif delete_choice == 4:
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
