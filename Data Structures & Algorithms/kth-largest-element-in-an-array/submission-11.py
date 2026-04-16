import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: 
        k=len(nums)-k

        def quickSelect(l,r):
            pivot = nums[r]
            i,j = l,r
            while i<j:
                while i<r and nums[i]<=pivot:
                    i+=1
                while j>l and nums[j]>=pivot:
                    j-=1
                if i<j:
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[r] = nums[r], nums[i]

            if k==i:
                return nums[i]
            elif k>i:
                return quickSelect(i+1, r)
            else:
                return quickSelect(l, i-1)

        return quickSelect(0, len(nums)-1)
                    
                