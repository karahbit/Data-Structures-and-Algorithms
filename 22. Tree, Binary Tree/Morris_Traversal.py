# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
