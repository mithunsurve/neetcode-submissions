class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev = 0
        curr =0

        for i in range(2, n+1):
            tmp = min(prev + cost[i-2], curr + cost[i-1])
            prev = curr
            curr = tmp

        return curr

            