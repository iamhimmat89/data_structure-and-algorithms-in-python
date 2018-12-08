print("\nWelcome to Queue(linked-list) Data Structure.!!!\n")

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


# Class Queue: Used for different operation en_queue, de_queue etc
class Queue:

    # constructor
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    # Method to insert a node at the end of the list
    def en_queue(self, data):
        new_node = Node()
        new_node.set_data(data)

        if self.length == 0:
            self.front = new_node
        else:
            self.rear.set_next(new_node)

        self.rear = new_node

        self.length += 1
        print(str(data) + " is successfully added to the queue")

    # Method to delete a node from the beginning of list
    def de_queue(self):
        if self.length == 0:
            print("Queue is empty\n")
        else:
            self.front = self.front.get_next()
            self.length -= 1
            print("node is deleted from the queue")

    # Method to display the list
    def display(self):
        if self.length == 0:
            print("Queue is empty\n")
        else:
            print("Queue: ")
            current = self.front

            while current is not None:
                print(str(current.data))
                current = current.get_next()


queue1 = Queue()

while True:
    print("Please enter Choice: ")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    print("")
    print("input: ")
    choice = int(input())

    if choice == 1:
        print("Please enter data to be insert: ")
        insert_data = int(input())
        queue1.en_queue(insert_data)
    elif choice == 2:
        queue1.de_queue()
    elif choice == 3:
        queue1.display()
    elif choice == 4:
        print("Good Bye..!!!")
        break
    else:
        print("Please enter valid input")
