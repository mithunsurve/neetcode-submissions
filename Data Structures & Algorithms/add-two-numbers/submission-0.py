# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def revSum(self, head):
        sum=0
        multiplier=1
        while head:
            sum=sum+(head.val * multiplier)
            multiplier*=10
            head=head.next
        return sum
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1=self.revSum(l1)
        sum2=self.revSum(l2)

        sum=sum1+sum2
        if sum==0:
            return ListNode(0)

        result=head=ListNode(0)
        while sum:
            node=ListNode(sum%10)
            sum=sum//10
            head.next=node
            head=head.next

        return result.next