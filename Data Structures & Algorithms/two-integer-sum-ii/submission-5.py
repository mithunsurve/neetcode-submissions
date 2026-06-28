class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer solution
        #initialize i=0 & j=n-1
        i,j=0,len(numbers)-1

        #while loop
        while i<j:
            sumIJ = (numbers[i]+numbers[j])
        #if the target is less thn (i+j) j=-1
            if target < sumIJ:
                j-=1
        #if the target is more thn (i+j) i+=1
            elif target > sumIJ:
                i+=1
        #if target == sumIJ, return i,j
            else:
                return [i+1, j+1]