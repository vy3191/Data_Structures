"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            return None
        
        if self.value <= value:
            if self.right is None:
                new_node = BSTNode(value)    
                self.right = new_node
            else:
                self.right.insert(value)    
        if self.value > value:
            if self.left is None:
                new_node = BSTNode(value)        
                self.left = new_node
            else:
                self.left.insert(value)    


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is None:
            return False

        if target is None:
            return None

        if self.value == target:
            return True

        if self.value < target:
            if self.right is None:
                return False
            elif self.right == target:
                return True    
            else:
                return self.right.contains(target)    

        if self.value > target:
            if self.left is None:
                return False
            elif self.left == target:
                return True    
            else:
                return self.left.contains(target)     

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value        
        else:
            return self.right.get_max()        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.value:
            fn(self.value)  
        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    def depth_first(self,fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)    
        if self.right:
            self.right.in_order_print()    

        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self,node):
        queue = deque()
        current = node
        queue.append(current)
        while len(queue) >0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)    
            print(current.value)    


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self,node):
        stack = deque()
        current = node
        stack.append(current)
        while len(stack) >0:
            current = stack.pop()
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)    
            print(current.value)    

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(14)
bst.insert(20)

bst.bft_print(bst)
bst.dft_print(bst)

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
