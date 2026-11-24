# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.minimum = float('inf')

        def inorder(node):
            if node is None:
                return 

            inorder(node.left)

            if self.prev is not None:
                difference = node.val - self.prev
                self.minimum = min(self.minimum,difference)

            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.minimum