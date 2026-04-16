# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:     
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for head in lists:
            curr = head
            while curr:
                minHeap.append(curr.val)
                curr = curr.next

        heapq.heapify(minHeap)
        dummy = curr = ListNode()
        while minHeap:
            node = ListNode(heapq.heappop(minHeap))
            curr.next = node
            curr = curr.next

        return dummy.next


