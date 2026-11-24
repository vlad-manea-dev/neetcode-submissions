# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
                0
            0       0
        0       00      0
    0       00  00  00      0

"""
class Solution:
    def minCameraCover(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return 2
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0 or right == 0:
                count += 1
                return 1
            if left == 2 and right == 2:
                return 0
            if left == 1 or right == 1:
                return 2

        
        return count + 1 if dfs(root) == 0 else count
            