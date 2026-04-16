from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a hashMap
        count = {}
        #count the number of occurences for each term
        for num in nums:
            count[num] = 1+count.get(num,0)
        #create a list for heap
        heap = []
        #for each key in hashMap
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res