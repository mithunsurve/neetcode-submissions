class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        profit=0
        minV=None
        maxV=0
        while j<len(prices):
            if prices[i]<prices[j]:
                profit = max(prices[j]-prices[i], profit)
            else:
                i=j
            j+=1
            

        return profit



