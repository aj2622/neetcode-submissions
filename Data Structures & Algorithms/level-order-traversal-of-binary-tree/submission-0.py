# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level = [root]
        ans = []
        while level:
            ans.append([node.val for node in level])
            newlevel = []
            for node in level:
                if node.left:
                    newlevel.append(node.left)
                if node.right:
                    newlevel.append(node.right)
            level = newlevel
        return ans
