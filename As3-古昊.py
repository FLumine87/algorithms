# R-6.5 Implement a function that reverses a list of elements by pushing them onto a 
# stack in one order, and writing them back to the list in reversed order.

def reverse_list(lst):
    stack = []
    for element in lst:
        stack.append(element)
    reversed_list = []
    while stack:
        reversed_list.append(stack.pop())
    return reversed_list

original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(reversed_list)

# R-6.13 Suppose you have a deque D containing the numbers (1,2,3,4,5,6,7,8), in this 
# order. Suppose further that you have an initially empty queue Q. Give a code fragment 
# that uses only D and Q (and no other variables) and results in D storing the elements 
# in the order (1,2,3,5,4,6,7,8). 

from collections import deque
D = deque([1, 2, 3, 4, 5, 6, 7, 8])
Q = deque()
D.append(D.popleft())  
D.append(D.popleft())  
D.append(D.popleft())  
Q.append(D.popleft())  
D.append(D.popleft())  
D.append(Q.popleft())  
D.append(D.popleft())
D.append(D.popleft())
D.append(D.popleft())
print(D)  

# C-6.24 Describe how to implement the stack ADT using a single queue as an instance 
# variable, and only constant additional local memory within the method bodies. What 
# is the running time of the push(), pop(), and top() methods for your design? 

# answer:When implementing a stack using a single queue, during each push operation of a new element, the new element is first enqueued, and then all existing elements in the queue are dequeued and re-enqueued one by one.
#  This ensures that the new element moves to the front of the queue (i.e., the top of the stack). 
# As a result, pop and top operations can be performed directly on the front element. 
# With this approach, the push operation has a time complexity of O(n), while both pop and top operations have a time complexity of O(1).

# C-6.25 Describe how to implement the queue ADT using two stacks as instance 
# variables, such that all queue operations execute in amortized O(1) time. 
# answer:To implement a queue using two stacks, we can use one stack (stack_in) for enqueue operations and another stack (stack_out) for dequeue operations.