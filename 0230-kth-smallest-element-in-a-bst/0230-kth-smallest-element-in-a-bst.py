# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        count = k
        res = root
        def dfs(node):
            nonlocal count, res
            if not node:
                return 
            dfs(node.left)
            count -= 1
            if count == 0:
                res = node.val
                return res
            dfs(node.right)
        dfs(root)
        return res