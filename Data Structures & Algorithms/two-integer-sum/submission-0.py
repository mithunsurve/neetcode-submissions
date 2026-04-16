class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a hashmap
        count = {}
        #loop through the nums array
        for i in range(len(nums)):
            #store the difference of target - num as key & index as value
            count[nums[i]] = i
        # loop through again 
        for i in range(len(nums)):
            #check if the difference exists in hashmap
            diff = target - nums[i]
            if diff in count:
                #if the index is same, continue
                if not i == count[diff]:
                    return [i, count[diff]]
