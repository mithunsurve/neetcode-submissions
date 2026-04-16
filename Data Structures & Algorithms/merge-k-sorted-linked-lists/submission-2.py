# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:     
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        counter = 0

        for head in lists:
            if head:
                heapq.heappush(minHeap, (head.val, counter, head))
                counter += 1

        dummy = curr = ListNode()

        while minHeap:
            _, _, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, counter, node.next))
                counter +=1

        return dummy.next


