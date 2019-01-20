
def search(arr, e):
    for i in range(len(arr)):
        if e == arr[i]:
            return i
    return -1


arr = [2, 3, 5, 6, 98, 23, 28, 56, 12, 7, 19]
result = search(arr, int(input("Enter value to search: ")))

if result == -1:
    print("Value in not present in array")
else:
    print("Values is present in array at index ", result)
