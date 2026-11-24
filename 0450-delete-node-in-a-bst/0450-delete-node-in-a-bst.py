# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        def successor(node):
            if node.right:
                cur = node.right
                while cur.left:
                    cur = cur.left
                return cur
            return node
        def dfs(node, key):
            if not node:
                return None
            if key < node.val:
                node.left = dfs(node.left, key)
            elif key > node.val:
                node.right = dfs(node.right, key)
            else:                                  # found it
                if not node.left:  return node.right
                if not node.right: return node.left
                succ = successor(node)        # both children exist
                node.val = succ.val
                node.right = dfs(node.right, succ.val)
            return node          
        return dfs(root, key)