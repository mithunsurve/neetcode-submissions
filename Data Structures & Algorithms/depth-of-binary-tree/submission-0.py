# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base case
        #if root is None return 0
        if root is None:
            return 0
        
        #recursively got to the left and add 1
        countL = 1 + self.maxDepth(root.left)

        #recursively go to the right and add 1
        countR = 1 + self.maxDepth(root.right)

        #return the max count
        return max(countL, countR)