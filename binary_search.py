
def search(arr, e):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == e:
            return True
        elif e < arr[mid]:
            return search(arr[:mid], e)
        else:
            return search(arr[mid+1:], e)


arr = [2, 3, 5, 6, 23, 28, 56, 98]
result = search(arr, int(input("Enter value to search: ")))

if result:
    print("Value in present in array")
else:
    print("Values is not present in array")
