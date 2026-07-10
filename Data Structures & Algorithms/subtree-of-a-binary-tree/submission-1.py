# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return check(p.left, q.left) and check(p.right, q.right)
            return False
        
        def preorder(node):
            if not node:
                return False
            if node.val == subRoot.val:
                if check(node, subRoot):
                    return True
            return preorder(node.left) or preorder(node.right)
        
        return preorder(root)
