class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev = 0
        curr = 0
        for num in nums:
            tmp = max(prev + num, curr)
            prev = curr
            curr = tmp

        return curr
