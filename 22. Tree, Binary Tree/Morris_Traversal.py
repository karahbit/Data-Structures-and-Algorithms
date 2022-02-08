class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def morris_traversal(root):
    curr = root
    res = []
    while curr:
        if curr.left:
            pre = curr.left
            while pre.right and pre.right is not curr:
                pre = pre.right
            if pre.right is curr:
                pre.right = None
                # res.append(curr.val)    # in-order
                curr = curr.right
            else:
                res.append(curr.val)    # pre-order and post-order
                pre.right = curr
                curr = curr.left
        else:
            res.append(curr.val)
            curr = curr.right

    # return res[::-1]    # post-order
    return res


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.left = tea
leftChild.right = coffee
rightChild = TreeNode("Cold")
newBT.left = leftChild
newBT.right = rightChild

print(morris_traversal(newBT))
