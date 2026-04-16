class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxSize=0
        while i<j:
            maxSize = max((j-i) * min(heights[i], heights[j]), maxSize)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return maxSize
