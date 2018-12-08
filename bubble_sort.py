print("\nWelcome to Bubble Sort...!!!\n")


# Class bubbleSort: Used for sorting given data
class BubbleSort:

    # constructor
    def __init__(self):
        self.swapped = False
        self.array = None
        self.length = None

    # method to sort given list into ascending order
    def sort(self, array):
        self.array = array
        self.length = len(array)

        for i in range(self.length):
            print("i loop - " + str(i))
            self.swapped = False
            for j in range(0, self.length - i - 1):
                print("    j loop - " + str(j))
                if self.array[j] > self.array[j + 1]:
                    print("    Swap :: " + str(self.array[j]) + " and " + str(self.array[j + 1]))
                    self.swapped = True
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

            print("    iteration output: " + str(self.array))
            if not self.swapped:
                break

    # method to display sorted array
    def display(self):
        print(str(self.array))


bsort = BubbleSort()
arr = [10, 20, 30, 15, 25, 5, 17, 2]
print("Input Array:: ")
print(str(arr))
print(" ")
bsort.sort(arr)
print(" ")
print("Sorted Array:: ")
bsort.display()