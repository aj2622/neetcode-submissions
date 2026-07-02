# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans = 0

        def dfs(node, depth):
            if not node:
                return 0
            
            if node.right:
                depth_right = dfs(node.right, depth+1)
            else:
                depth_right = depth
            if node.left:
                depth_left = dfs(node.left, depth+1)
            else:
                depth_left = depth
            
            nonlocal ans
            ans = max(ans, depth_left+depth_right-2*depth)
            
            return max(depth_right, depth_left)
        
        dfs(root,1)

        return ans
            
