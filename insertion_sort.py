print("\nWelcome to Insertion Sort...!!!\n")


# Class insertionSort: Used for sorting given data
class InsertionSort:

    # constructor
    def __init__(self):
        self.array = None
        self.length = None

    # method to sort given list into ascending order
    def sort(self, array):
        self.array = array
        self.length = len(array)

        for i in range(1, self.length):
            key = self.array[i]
            print("i loop - " + str(i))

            j = i - 1
            while j >= 0 and key < self.array[j]:
                print("    j loop - " + str(j))
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
            print("    iteration output: " + str(self.array))

    # method to display sorted array
    def display(self):
        print(str(self.array))


isort = InsertionSort()
arr = [10, 20, 30, 15, 25, 5, 17, 2]
print("Input Array:: ")
print(str(arr))
print(" ")
isort.sort(arr)
print(" ")
print("Sorted Array:: ")
isort.display()
