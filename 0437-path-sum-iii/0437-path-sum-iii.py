# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix = {0: 1}                         # prefix sum -> count, on the current root-to-node path
        def dfs(node, cur):                     # returns: number of valid paths ending inside this subtree
            if not node:
                return 0
            cur += node.val                     # 1. include this node first
            count = prefix.get(cur - targetSum, 0)          # paths ending HERE
            prefix[cur] = prefix.get(cur, 0) + 1            # 2. add before going down
            count += dfs(node.left, cur) + dfs(node.right, cur)
            prefix[cur] -= 1                    # 3. undo on the way back up
            return count
        return dfs(root, 0)