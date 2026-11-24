# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        q = collections.deque([root])
        if not root:
            return []
        res = []
        left_to_right = True
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()               # always pop left, so levels never mix
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level if left_to_right else level[::-1])
            left_to_right = not left_to_right    # flip ONCE per level
        return res

