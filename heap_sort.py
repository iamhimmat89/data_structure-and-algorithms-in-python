print("\nWelcome to Heap Sort...!!!\n")


# Class heapSort: Used for sorting given data
class HeapSort:

    # constructor
    def __init__(self):
        self.array = None

    # build max heap
    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.array[i] < self.array[l]:
            largest = l

        if r < n and self.array[largest] < self.array[r]:
            largest = r

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.heapify(n, largest)

    # method to sort given list into ascending order
    def sort(self, array):
        self.array = array
        n = len(self.array)

        for i in range(n, -1, -1):
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(i, 0)

    # method to display sorted array
    def display(self):
        print(str(self.array))


hsort = HeapSort()
arr = [10, 20, 30, 15, 25, 5, 17, 2]
print("Input Array:: ")
print(str(arr))
print(" ")
hsort.sort(arr)
print(" ")
print("Sorted Array:: ")
hsort.display()
