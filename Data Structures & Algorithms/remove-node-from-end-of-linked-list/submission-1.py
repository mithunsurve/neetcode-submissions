# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None:
            return None
        curr=head
        counter=0
        while curr:
            counter+=1
            curr=curr.next

        counter=counter-n
        if not counter:
            return head.next
        curr=head
        while counter>1:
            curr=curr.next
            counter-=1

        next_node=curr.next
        curr.next=next_node.next

        return head


        