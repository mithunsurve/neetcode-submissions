# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def maxHeight(root):
            if root is None:
                return 0

            heghtL=maxHeight(root.left)
            heightR=maxHeight(root.right)

            self.res=max(self.res, heghtL+heightR)

            return 1+max(heghtL,heightR)

        maxHeight(root)

        return self.res