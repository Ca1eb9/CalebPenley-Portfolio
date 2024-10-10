# LAB 4
#CP
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    """
        >>> my_tree = BinarySearchTree()
        >>> my_tree.isEmpty()
        True
        >>> my_tree.isBalanced
        True
        >>> my_tree.insert(9)
        >>> my_tree.insert(5)
        >>> my_tree.get_numLeaves()
        1
        >>> my_tree.insert(14)
        >>> my_tree.insert(4)
        >>> my_tree.insert(6)
        >>> my_tree.get_numLeaves()
        3
        >>> my_tree.insert(5.5)
        >>> my_tree.insert(7)
        >>> my_tree.insert(25)
        >>> my_tree.insert(23)
        >>> my_tree.getMin
        4
        >>> my_tree.getMax
        25
        >>> 67 in my_tree
        False
        >>> 5.5 in my_tree
        True
        >>> my_tree.isEmpty()
        False
        >>> my_tree.getHeight(my_tree.root)   # Height of the tree
        3
        >>> my_tree.getHeight(my_tree.root.left.right)
        1
        >>> my_tree.getHeight(my_tree.root.right)
        2
        >>> my_tree.getHeight(my_tree.root.right.right)
        1
        >>> my_tree.isBalanced
        False
        >>> my_tree.insert(10)
        >>> my_tree.isBalanced
        True
        >>> my_tree.get_numLeaves()
        5
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    

    def isEmpty(self): #Determines if tree is empty
        # YOUR CODE STARTS HERE
        if self.root == None: #If there is no root, the tree is empty
            return True
        else:
            return False


    @property
    def getMin(self): #Gets min value in tree
        # YOUR CODE STARTS HERE
        if self.root == None:
            return None
        current = self.root
        while current.left:#Go down left until we hit the min value
            current = current.left
        return current.value

        


    @property
    def getMax(self): #Gets max value in tree
        # YOUR CODE STARTS HERE
        if self.root == None:
            return None
        current = self.root
        while current.right:#Go down right until we hit max value
            current = current.right
        return current.value


    def __contains__(self,value): #checks whether a value is in tree
        # YOUR CODE STARTS HERE
        if self.root == None:
            return False
        current = self.root
        while current: #Checks through each node, if node is higher than node, go left, else, go right, and repeat until there either is an equal value, or it returns false
            if current.value > value:
                current = current.left
            elif current.value == value:
                return True
            else:
                current = current.right

        return False


    def getHeight(self, node): #gets height of tree by finding all heights
        # YOUR CODE STARTS HERE
        if node is None:
            return -1
        left = self.getHeight(node.left) #gets height of all branches in left
        right = self.getHeight(node.right) #gets height of all branches in right
        return max(left, right) +1 #returns highest height


    def get_numLeaves(self): # Do not modify this method
        return self._get_numLeaves_helper(self.root)


    def _get_numLeaves_helper(self, node):#gets number of leaves by recursivly counting leaves
        # YOUR CODE STARTS HERE
        if node is None:
            return 0
        if node.left is None and node.right is None:#Leaf
            return 1
        return self._get_numLeaves_helper(node.left) + self._get_numLeaves_helper(node.right)#adds up the leaves
        

    @property
    def isBalanced(self):  # Do not modify this method
        return self.isBalanced_helper(self.root)
    
    
    def isBalanced_helper(self, node):#checks of tree is balanced by recursivly called itself and checking heights of branches, or its false
        # YOUR CODE STARTS HERE
        if node is None:
            return True
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)

        if abs(left - right) <=1:
            return self.isBalanced_helper(node.left) and self.isBalanced_helper(node.right)#recursion, possibly returning True
        else:
            return False #else False


def run_tests():
    import doctest
    doctest.testmod(verbose=True)
    
if __name__ == "__main__":
    run_tests()