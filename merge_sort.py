print("\nWelcome to Merge Sort...!!!\n")


# Class mergeSort: Used for sorting given data
class MergeSort:

    # constructor
    def __init__(self):
        self.array = None

    # method to sort given list into ascending order
    def sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            L = array[:mid]
            R = array[mid:]

            self.sort(L)
            self.sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    array[k] = L[i]
                    i = i + 1
                else:
                    array[k] = R[j]
                    j = j + 1
                k = k + 1

            while i < len(L):
                array[k] = L[i]
                i = i + 1
                k = k + 1

            while j < len(R):
                array[k] = R[j]
                j = j + 1
                k = k + 1

        self.array = array

    # method to display sorted array
    def display(self):
        print(str(self.array))


msort = MergeSort()
arr = [10, 20, 30, 15, 25, 5, 17, 2]
print("Input Array:: ")
print(str(arr))
print(" ")
msort.sort(arr)
print(" ")
print("Sorted Array:: ")
msort.display()
