# Algorithms:
# Bubble Sort:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]      
bubble_sort(arr)        
print("Sorted array:", arr)

# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

# The math involved in bubble sort primarily concerns the number of comparisons and swaps required to sort the list. 

# While bubble sort is simple to understand and implement, it is not efficient for large lists due to its quadratic time complexity. Other sorting algorithms like quicksort, mergesort, and heapsort are more efficient for larger datasets. However, bubble sort can still be useful for small lists or as a teaching tool to understand sorting algorithms and concepts like comparisons and swaps.


# Linear Search:
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1

# Example usage
arr = [2, 3, 4, 10, 40]
target = 10 
result = linear_search(arr, target)
if result != 1: 
    print("Element", target, "is present at index", result)
else:
    print("Element", target, "is not present in array")

# Linear search, also known as sequential search, is a simple searching algorithm that sequentially checks each element in a list or array until the target element is found or the end of the list is reached. It works well for small lists or unsorted arrays but is inefficient for large lists or sorted arrays compared to more advanced search algorithms like binary search.

# These examples provide a basic understanding of how to implement data structures and algorithms in Python 3. You can further explore and expand upon these concepts based on your requirements and the problem you are trying to solve.
    