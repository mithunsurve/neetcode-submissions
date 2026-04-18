class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxCount = 0
        
        for num in hashSet:
            if (num-1) not in hashSet:
                count = 1
                while (num+count) in hashSet:
                    count+=1
                maxCount = max(maxCount, count)
        return maxCount