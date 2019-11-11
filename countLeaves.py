
#Initial Template for Python 3
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
        
        
 def countLeaves(root):
    if root is None:
        return 0
    elif (root.left is None) and (root.right is None):
        return 1
    else :
        return countLeaves(root.left) + countLeaves(root.right)
        
#Implement driver code on your own
