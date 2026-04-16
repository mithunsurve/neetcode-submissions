import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.minHeap = heapq.nlargest(self.k, self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        return heapq.nlargest(self.k, self.minHeap)[-1]

