# Python Algorithms & Data Structure

**1.  	Singly linked list - linked_list.py**
		- 	Insert node to list
			- Insert node at the beginning of the list
			- Insert node at the end of the list
			- Insert node at particular position in the list
		- 	Delete node from list
			- Delete node from the beginning of the list
			- Delete last node from the list
			- Delete node from particular position
			- Delete value from the list
		- 	Display list
		- 	Search node in list
		- 	Clear list
		- 	Exit
	
**2.  	Doubly linked list - doubly_linked_list.py**
		- 	Insert node to list
			- Insert node at the beginning of the list
			- Insert node at the end of the list
			- Insert node at particular position in the list
		- 	Delete node from list
			- Delete node from the beginning of the list
			- Delete last node from the list
			- Delete node from particular position
			-iv. Delete value from the list
		- 	Display list
		- 	Search node in list
		- 	Clear list
		- 	Exit
	
**3.  	Circular linked list - circular_linked_list.py**
		- 	Insert node to list
		- 	Delete node from list
			- Delete node from the list
			- Node value to be delete from the list
		- 	Display list
		- 	Search node in list
		- 	Clear list
		- 	Exit
	
**4.  	Stack - stack.py**
		- 	Push
		- 	Pop
		- 	Display
		- 	Exit
	
**5.  	Queue - queue.py**
		- 	Enqueue
		- 	Dequeue
		- 	Display
		- 	Exit
	

## **Sorting Algorithms**

**1. Bubble Sort - bubble_sort.py**
	 - Sample Output
```
Input Array:: 
[10, 20, 30, 15, 25, 5, 17, 2]
 
i loop - 0
    j loop - 0
    j loop - 1
    j loop - 2
    Swap :: 30 and 15
    j loop - 3
    Swap :: 30 and 25
    j loop - 4
    Swap :: 30 and 5
    j loop - 5
    Swap :: 30 and 17
    j loop - 6
    Swap :: 30 and 2
    iteration output: [10, 20, 15, 25, 5, 17, 2, 30]
i loop - 1
    j loop - 0
    j loop - 1
    Swap :: 20 and 15
    j loop - 2
    j loop - 3
    Swap :: 25 and 5
    j loop - 4
    Swap :: 25 and 17
    j loop - 5
    Swap :: 25 and 2
    iteration output: [10, 15, 20, 5, 17, 2, 25, 30]
i loop - 2
    j loop - 0
    j loop - 1
    j loop - 2
    Swap :: 20 and 5
    j loop - 3
    Swap :: 20 and 17
    j loop - 4
    Swap :: 20 and 2
    iteration output: [10, 15, 5, 17, 2, 20, 25, 30]
i loop - 3
    j loop - 0
    j loop - 1
    Swap :: 15 and 5
    j loop - 2
    j loop - 3
    Swap :: 17 and 2
    iteration output: [10, 5, 15, 2, 17, 20, 25, 30]
i loop - 4
    j loop - 0
    Swap :: 10 and 5
    j loop - 1
    j loop - 2
    Swap :: 15 and 2
    iteration output: [5, 10, 2, 15, 17, 20, 25, 30]
i loop - 5
    j loop - 0
    j loop - 1
    Swap :: 10 and 2
    iteration output: [5, 2, 10, 15, 17, 20, 25, 30]
i loop - 6
    j loop - 0
    Swap :: 5 and 2
    iteration output: [2, 5, 10, 15, 17, 20, 25, 30]
i loop - 7
    iteration output: [2, 5, 10, 15, 17, 20, 25, 30]
 
Sorted Array:: 
[2, 5, 10, 15, 17, 20, 25, 30]
```

**2. Insertion Sort - insertion_sort.py**
	 - Sample Output
```
Input Array:: 
[10, 20, 30, 15, 25, 5, 17, 2]
 
i loop - 1
    iteration output: [10, 20, 30, 15, 25, 5, 17, 2]
i loop - 2
    iteration output: [10, 20, 30, 15, 25, 5, 17, 2]
i loop - 3
    j loop - 2
    j loop - 1
    iteration output: [10, 15, 20, 30, 25, 5, 17, 2]
i loop - 4
    j loop - 3
    iteration output: [10, 15, 20, 25, 30, 5, 17, 2]
i loop - 5
    j loop - 4
    j loop - 3
    j loop - 2
    j loop - 1
    j loop - 0
    iteration output: [5, 10, 15, 20, 25, 30, 17, 2]
i loop - 6
    j loop - 5
    j loop - 4
    j loop - 3
    iteration output: [5, 10, 15, 17, 20, 25, 30, 2]
i loop - 7
    j loop - 6
    j loop - 5
    j loop - 4
    j loop - 3
    j loop - 2
    j loop - 1
    j loop - 0
    iteration output: [2, 5, 10, 15, 17, 20, 25, 30]
 
Sorted Array:: 
[2, 5, 10, 15, 17, 20, 25, 30]
```

**3. Selection Sort - selection_sort.py**
	 - Sample Output
```
Input Array:: 
[10, 20, 30, 15, 25, 5, 17, 2]
 
iteration output: [2, 20, 30, 15, 25, 5, 17, 10]
iteration output: [2, 5, 30, 15, 25, 20, 17, 10]
iteration output: [2, 5, 10, 15, 25, 20, 17, 30]
iteration output: [2, 5, 10, 15, 25, 20, 17, 30]
iteration output: [2, 5, 10, 15, 17, 20, 25, 30]
iteration output: [2, 5, 10, 15, 17, 20, 25, 30]
iteration output: [2, 5, 10, 15, 17, 20, 25, 30]
iteration output: [2, 5, 10, 15, 17, 20, 25, 30]
 
Sorted Array:: 
[2, 5, 10, 15, 17, 20, 25, 30]
```

**4. Quick Sort - quick_sort.py**
	 - Sample Output
```
Input Array:: 
[10, 20, 30, 15, 25, 5, 7, 2]
 
    swap_outside 10 and 2
    array: [2, 20, 30, 15, 25, 5, 7, 10]
    swap_inside 20 and 5
    array: [2, 5, 30, 15, 25, 20, 7, 10]
    swap_inside 30 and 7
    array: [2, 5, 7, 15, 25, 20, 30, 10]
    swap_outside 15 and 10
    array: [2, 5, 7, 10, 25, 20, 30, 15]
    swap_inside 5 and 5
    array: [2, 5, 7, 10, 25, 20, 30, 15]
    swap_outside 7 and 7
    array: [2, 5, 7, 10, 25, 20, 30, 15]
    swap_outside 25 and 15
    array: [2, 5, 7, 10, 15, 20, 30, 25]
    swap_inside 20 and 20
    array: [2, 5, 7, 10, 15, 20, 30, 25]
    swap_outside 30 and 25
    array: [2, 5, 7, 10, 15, 20, 25, 30]
 
Sorted Array:: 
[2, 5, 7, 10, 15, 20, 25, 30]
```

**5. Merge Sort - merge_sort.py**
	 - Sample Output
```
Input Array:: 
[10, 20, 30, 15, 25, 5, 17, 2]
 
mid: 4
L: [10, 20, 30, 15]
R: [25, 5, 17, 2]
mid: 2
L: [10, 20]
R: [30, 15]
mid: 1
L: [10]
R: [20]
    iteration output: [10, 20]
mid: 1
L: [30]
R: [15]
    iteration output: [15, 30]
    iteration output: [10, 15, 20, 30]
mid: 2
L: [25, 5]
R: [17, 2]
mid: 1
L: [25]
R: [5]
    iteration output: [5, 25]
mid: 1
L: [17]
R: [2]
    iteration output: [2, 17]
    iteration output: [2, 5, 17, 25]
    iteration output: [2, 5, 10, 15, 17, 20, 25, 30]
 
Sorted Array:: 
[2, 5, 10, 15, 17, 20, 25, 30]
```

**5. Heap Sort - heap_sort.py**
	 - Sample Output
```
Input Array:: 
[10, 20, 30, 15, 25, 5, 17, 2]
 
largest : 8
l : 17
r : 18
largest : 7
l : 15
r : 16
largest : 6
l : 13
r : 14
largest : 5
l : 11
r : 12
largest : 4
l : 9
r : 10
largest : 3
l : 7
r : 8
largest : 2
l : 5
r : 6
largest : 1
l : 3
r : 4
iteration output : [10, 25, 30, 15, 20, 5, 17, 2]
largest : 4
l : 9
r : 10
largest : 0
l : 1
r : 2
iteration output : [30, 25, 10, 15, 20, 5, 17, 2]
largest : 2
l : 5
r : 6
iteration output : [30, 25, 17, 15, 20, 5, 10, 2]
largest : 6
l : 13
r : 14
largest : 0
l : 1
r : 2
iteration output : [25, 2, 17, 15, 20, 5, 10, 30]
largest : 1
l : 3
r : 4
iteration output : [25, 20, 17, 15, 2, 5, 10, 30]
largest : 4
l : 9
r : 10
iteration output : [25, 20, 17, 15, 2, 5, 10, 30]
largest : 0
l : 1
r : 2
iteration output : [20, 10, 17, 15, 2, 5, 25, 30]
largest : 1
l : 3
r : 4
iteration output : [20, 15, 17, 10, 2, 5, 25, 30]
largest : 3
l : 7
r : 8
iteration output : [20, 15, 17, 10, 2, 5, 25, 30]
largest : 0
l : 1
r : 2
iteration output : [17, 15, 5, 10, 2, 20, 25, 30]
largest : 2
l : 5
r : 6
iteration output : [17, 15, 5, 10, 2, 20, 25, 30]
largest : 0
l : 1
r : 2
iteration output : [15, 2, 5, 10, 17, 20, 25, 30]
largest : 1
l : 3
r : 4
iteration output : [15, 10, 5, 2, 17, 20, 25, 30]
largest : 3
l : 7
r : 8
iteration output : [15, 10, 5, 2, 17, 20, 25, 30]
largest : 0
l : 1
r : 2
iteration output : [10, 2, 5, 15, 17, 20, 25, 30]
largest : 1
l : 3
r : 4
iteration output : [10, 2, 5, 15, 17, 20, 25, 30]
largest : 0
l : 1
r : 2
iteration output : [5, 2, 10, 15, 17, 20, 25, 30]
largest : 0
l : 1
r : 2
iteration output : [2, 5, 10, 15, 17, 20, 25, 30]
 
Sorted Array:: 
[2, 5, 10, 15, 17, 20, 25, 30]
```