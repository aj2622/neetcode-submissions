# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node, min, max):
            if node is None:
                return True
            if node.val >= max or node.val <= min:
                return False
            return check(node.right, node.val, max) and check(node.left, min, node.val) 
                
        return check(root,-float('inf'), float('inf'))