# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        #initialise slow,fast = head
        slow=head
        fast=head.next
        #while fast.next.next:
        while fast:
            #if fast==slow:
            if fast == slow:
                #return True
                return True
            #slow = slow.next
            slow = slow.next
            #fast = fast.next.next
            if(fast.next) is None:
                return False
            else:
                fast = fast.next.next

        #return False
        return False