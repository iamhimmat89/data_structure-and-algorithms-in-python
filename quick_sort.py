print("\nWelcome to Insertion Sort...!!!\n")


# Class quick_sort: Used for sorting given data
class QuickSort:

    # constructor
    def __init__(self):
        self.array = None
        self.length = None

    def partition(self, p, r):
        i = p - 1

        for j in range(p, r):
            if self.array[j] <= self.array[r]:
                i = i + 1
                self.array[i], self.array[j] = self.array[j], self.array[i]

        self.array[i + 1], self.array[r] = self.array[r], self.array[i + 1]
        return i + 1

    def sort(self, p, r, array=None):
        if array is not None:
            self.array = array

        if p < r:
            q = self.partition(p, r)
            self.sort(p, q-1)
            self.sort(q+1, r)

    # method to display sorted array
    def display(self):
        print(str(self.array))


qsort = QuickSort()
arr = [10, 20, 30, 15, 25, 5, 7, 2]
arr_length = len(arr)
print("Input Array:: ")
print(str(arr))
print(" ")
qsort.sort(0, arr_length-1, arr)
print(" ")
print("Sorted Array:: ")
qsort.display()
