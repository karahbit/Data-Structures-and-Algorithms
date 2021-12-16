# A Python3 program to find value of the
# deepest node in a given binary tree
class new_Node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

# Utility function to find height
# of a tree, rooted at 'root'.


def height(root):
    if(not root):
        return 0

    leftHt = height(root.left)
    rightHt = height(root.right)

    return max(leftHt, rightHt) + 1

# levels : current Level
# Utility function to print all
# nodes at a given level.


def deepestNode(root, levels):
    if(not root):
        return

    if(levels == 1):
        print(root.data)
    elif(levels > 1):
        deepestNode(root.left, levels - 1)
        deepestNode(root.right, levels - 1)


# Driver Code
if __name__ == '__main__':

    root = new_Node(1)
    root.left = new_Node(2)
    root.right = new_Node(3)
    root.left.left = new_Node(4)
    root.right.left = new_Node(5)
    root.right.right = new_Node(6)
    root.right.left.right = new_Node(7)
    root.right.right.right = new_Node(8)
    root.right.left.right.left = new_Node(9)

    # Calculating height of tree
    levels = height(root)
    print(levels)

    # Printing the deepest node
    deepestNode(root, levels)

# This code is contributed by PranchalK
