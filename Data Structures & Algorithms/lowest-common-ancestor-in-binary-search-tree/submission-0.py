# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        ans = None
        def dfs(node):
            nonlocal ans
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node.val == p.val or node.val == q.val
            if mid:
                print(node.val)
            if left + right + mid >= 2:
                ans = node
            return left or right or mid
        dfs(root)
        return ans