class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        total = 1
        for num in nums:
            total *= num
            prefix.append(int(total))

        postfix = [1] * len(nums)
        total = 1
        for i in range(len(nums)-1, -1, -1):
            total *= nums[i]
            postfix[i] = total

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(postfix[i+1])
            elif i==len(nums)-1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1] * postfix[i+1])

        return result
            