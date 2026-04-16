class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroExists = 0
        for num in nums:
            if num == 0:
                zeroExists +=1
                continue
            total *= num
        result = []

        if zeroExists > 1:
            return [0] * len(nums)

        for num in nums:
            if num == 0:
                result.append(int(total))
            elif zeroExists == 1:
                result.append(0)
            else:
                result.append(int(total/num))

        return result