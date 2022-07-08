Link - https://www.fullstack.cafe/blog/binary-tree-interview-questions

  
 ########################################################################################################################################################

1) Height of Binary Tree


# Python3 program to find the maximum depth of tree
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node
def maxDepth(node):
    if node is None:
        return 0 ;
 
    else :
 
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
 
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
 
print ("Height of tree is %d" %(maxDepth(root)))

Time Complexity: O(n) 
Auxiliary Space: O(n) due to recursive calls.
  
___________________________________________________________________________________________________________________
  
  Method 2: Another method to solve this problem is to do Level Order Traversal.
    
# Python code to implement the approach
 
# A Tree node
class Node:
 
    def __init__(self):
        self.key = 0
        self.left,self.right = None,None
 
# Utility function to create a new node
def newNode(key):
 
    temp = Node()
    temp.key = key
    temp.left,temp.right = None,None
    return temp
 
 
# Function to find the height(depth) of the tree
def height(root):
 
    #Initialising a variable to count the
    #height of tree
    depth = 0
 
    q = []
     
    #appending first level element along with None
    q.append(root)
    q.append(None)
    while(len(q)>0):
        temp = q[0]
        q = q[1:]
     
        #When None encountered, increment the value
        if(temp == None):
            depth += 1
         
        #If None not encountered, keep moving
        if(temp != None):
            if(temp.left):
                q.append(temp.left)
             
            if(temp.right):
                q.append(temp.right)
             
     
        #If queue still have elements left,
        #append None again to the queue.
        elif(len(q)>0):
            q.append(None)
    return depth
 
# Driver program
 
# Let us create Binary Tree shown in above example
root = newNode(1)
root.left = newNode(12)
root.right = newNode(13)
 
root.right.left = newNode(14)
root.right.right = newNode(15)
 
root.right.left.left = newNode(21)
root.right.left.right = newNode(22)
root.right.right.left = newNode(23)
root.right.right.right = newNode(24)
 
print(f"Height(Depth) of tree is: {height(root)}")

########################################################################################################################################################

2)Determine if two trees are identical


# Python program to determine if two trees are identical
 
# A binary tree node has data, pointer to left child
# and a pointer to right child
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
     
 
# Given two trees, return true if they are structurally
# identical
def identicalTrees(a, b):
     
    # 1. Both empty
    if a is None and b is None:
        return True
 
    # 2. Both non-empty -> Compare them
    if a is not None and b is not None:
        return ((a.data == b.data) and
                identicalTrees(a.left, b.left)and
                identicalTrees(a.right, b.right))
     
    # 3. one empty, one not -- false
    return False
 
# Driver program to test identicalTress function
root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
 
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
 
if identicalTrees(root1, root2):
    print("Both trees are identical")
else:
    print ("Trees are not identical")
    
########################################################################################################################################################

3)Mirror tree


# Python3 program to convert a binary
# tree to its mirror
 
# Utility function to create a new
# tree node
class newNode:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
 
""" Change a tree so that the roles of the
    left and right pointers are swapped at
    every node.
 
So the tree...
        4
        / \
    2 5
    / \
    1 3
 
is changed to...
    4
    / \
    5 2
    / \
    3 1
"""
def mirror(node):
 
    if (node == None):
        return
    else:
 
        temp = node
         
        """ do the subtrees """
        mirror(node.left)
        mirror(node.right)
 
        """ swap the pointers in this node """
        temp = node.left
        node.left = node.right
        node.right = temp
 
""" Helper function to print Inorder traversal."""
def inOrder(node) :
 
    if (node == None):
        return
         
    inOrder(node.left)
    print(node.data, end = " ")
    inOrder(node.right)
 
# Driver code
if __name__ =="__main__":
 
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
 
    """ Print inorder traversal of
        the input tree """
    print("Inorder traversal of the",
               "constructed tree is")
    inOrder(root)
     
    """ Convert tree to its mirror """
    mirror(root)
 
    """ Print inorder traversal of
        the mirror tree """
    print("\nInorder traversal of",
              "the mirror treeis ")
    inOrder(root)
________________________________________________________________________________________________________________


Method 2- Iterative

# Python3 program to convert a Binary
# Tree to its mirror
 
# A binary tree node has data, pointer to
# left child and a pointer to right child
# Helper function that allocates a new node
# with the given data and None left and
# right pointers
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
''' Change a tree so that the roles of the left
    and right pointers are swapped at every node.
    So the tree...
        4
        / \
        2 5
        / \
    1 3
     
    is changed to...
        4
        / \
        5 2
            / \
        3 1
    '''
     
def mirror( root):
 
    if (root == None):
        return
 
    q = []
    q.append(root)
 
    # Do BFS. While doing BFS, keep swapping
    # left and right children
    while (len(q)):
 
        # pop top node from queue
        curr = q[0]
        q.pop(0)
 
        # swap left child with right child
        curr.left, curr.right = curr.right, curr.left
 
        # append left and right children
        if (curr.left):
            q.append(curr.left)
        if (curr.right):
            q.append(curr.right)
 
""" Helper function to print Inorder traversal."""
def inOrder( node):
    if (node == None):
        return
    inOrder(node.left)
    print(node.data, end = " ")
    inOrder(node.right)
 
# Driver code
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
 
""" Print inorder traversal of the input tree """
print("Inorder traversal of the constructed tree is")
inOrder(root)
 
""" Convert tree to its mirror """
mirror(root)
 
""" Print inorder traversal of the mirror tree """
print("\nInorder traversal of the mirror tree is")
inOrder(root)

########################################################################################################################################################
4)Symmetric Tree
########################################################################################################################################################
5)
########################################################################################################################################################
6)
########################################################################################################################################################
7)
########################################################################################################################################################
8)
########################################################################################################################################################
9)
########################################################################################################################################################
10)
########################################################################################################################################################
    
    
   
_____________________________________________________________________________________________________________







