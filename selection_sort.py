print("\nWelcome to Selection Sort...!!!\n")


# Class selectionSort: Used for sorting given data
class SelectionSort:

    # constructor
    def __init__(self):
        self.array = None

    # method to sort given list into ascending order
    def sort(self, array):
        self.array = array
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i + 1, len(self.array)):
                if self.array[min_idx] > self.array[j]:
                    min_idx = j

            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            print("iteration output: " + str(self.array))

    # method to display sorted array
    def display(self):
        print(str(self.array))


ssort = SelectionSort()
arr = [10, 20, 30, 15, 25, 5, 17, 2]
print("Input Array:: ")
print(str(arr))
print(" ")
ssort.sort(arr)
print(" ")
print("Sorted Array:: ")
ssort.display()
