class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)

        l, r = 1, max(piles)
        while l<=r:
            mid=(l+r)//2
            totalTime=0
            for pile in piles:
                totalTime+= math.ceil(pile/mid)
            if totalTime <= h:
                result=mid
                r=mid-1
            else:
                l=mid+1

        return result
        