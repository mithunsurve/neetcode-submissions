# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #create a set
        nodeSet = set()

        current = head
        #traverse through the linked-list
        while current:
            #if the set already has a node then return true
            if current in nodeSet:
                return True
            #add each node to the set
            nodeSet.add(current)
            current = current.next
            
        #return false
        return False