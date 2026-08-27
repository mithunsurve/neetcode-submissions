# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #create a 2 queue for bfs
        #append rootP to queue1 and rootQ to queue2
        queueP = deque([p])
        queueQ = deque([q])

        #while queue1 and queue2
        while queueP and queueQ:
            #popleft() for queue1 & queue2
            nodeP = queueP.popleft()
            nodeQ = queueQ.popleft()

            #check if just one is none
            if nodeP is None and nodeQ is None:
                continue
            #if they are not same:
            if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                return False
                #return False

            #else:
            else:
                # append popleft's left & right for Q1 & Q2
                queueP.append(nodeP.left)
                queueQ.append(nodeQ.left)
                queueP.append(nodeP.right)
                queueQ.append(nodeQ.right)
                
                

        #return True
        if queueP or queueQ:
            return False
        return True