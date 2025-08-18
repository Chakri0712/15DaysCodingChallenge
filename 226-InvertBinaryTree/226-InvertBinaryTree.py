# Last updated: 8/18/2025, 9:22:34 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        self.invertTree(root.right)
        self.invertTree(root.left)
        root.right, root.left = root.left, root.right
        return root
        