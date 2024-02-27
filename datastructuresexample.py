# Data Structures:

# Arrays:

# Creating an array
array = [1, 2, 3, 4, 5]

# Accessing elements
print(array[0]) # Output: 1

# Modifying elements
array[0] = 10
print(array) # Output: [10, 2, 3, 4, 5]

# Length of the array
print(len(array)) # Output: 5

# Arrays are a contiguous block of memory that stores elements of the same data type. Examples include lists in Python, arrays in languages like C, Java, and JavaScript.

# Linked Lists:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
node1 = Node(1)
node2 = Node(2)  # Define node2
node3 = Node(3)  # Define node3

# Connecting nodes
node1.next = node2
node2.next = node3

# Traversing linked list
current = node1
while current:
    print(current.data)
    current = current.next

# A Linked List is a data structure consisting of a sequence of elements called nodes. Each node contains 2 parts such as data and a reference or pointer (to the next node in the sequence). Linked lists do not require contigious memory allocation and can be scattered in memory and connected via pointers. 
# Linked lists can be singly linked where each node points to the next node, doubly linked where each node has pointers to both the next and previous nodes, and circular linked lists where the last node points back the first node. 
# Examples of linked lists include implementations in languages like C, C++, Java, and Python.
