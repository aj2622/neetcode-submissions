# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node, depth):
            if not node:
                return depth
            if node.right:
                r_depth = dfs(node.right, depth+1)
            else:
                r_depth = depth
            if node.left:
                l_depth = dfs(node.left, depth+1)
            else:
                l_depth = depth
            return max(l_depth, r_depth)
                
        return dfs(root,1)