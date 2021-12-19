#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# List of Depth
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        if self.next:
            return "({val})".format(val=self.val) + str(self.next)
        else:
            return "({val})".format(val=self.val)


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# def depth(tree):
#     if tree == None:
#         return 0
#     if tree.left == None  and tree.right == None:
#         return 1
#     else:
#         depthLeft = 1 + depth(tree.left)
#         depthRight = 1 + depth(tree.right)
#         if depthLeft > depthRight:
#             return depthLeft
#         else:
#             return depthRight

# def treeToLinkedList(tree, custDict = {}, d = None):
#     if d == None:
#         d = depth(tree)
#     if custDict.get(d) == None:
#         custDict[d] = LinkedList(tree.val)
#     else:
#         custDict[d].add(tree.val)
#         if d == 1:
#             return custDict
#     if tree.left != None:
#         custDict = treeToLinkedList(tree.left, custDict, d-1)
#     if tree.right != None:
#         custDict = treeToLinkedList(tree.right, custDict, d-1)
#     return custDict


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def treeToLinkedList(root, level=1, max_level=None, custom_dc={}):
    if max_level is None:
        max_level = height(root)
    if level not in custom_dc:
        custom_dc[level] = LinkedList(root.val)
    else:
        custom_dc[level].add(root.val)
    if level == max_level:
        return custom_dc
    if root.left:
        custom_dc = treeToLinkedList(
            root.left, level + 1, max_level, custom_dc)
    if root.right:
        custom_dc = treeToLinkedList(
            root.right, level + 1, max_level, custom_dc)
    return custom_dc


mainTree = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)
mainTree.left = two
mainTree.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

custDict = treeToLinkedList(mainTree)
# print(custDict[3])
# print(custDict[2])
# print(custDict[1])
# for depthLevel, linkedList in custDict.items():
#     print("{0} {1}".format(depthLevel, linkedList))
for level in custDict:
    print(custDict[level])
