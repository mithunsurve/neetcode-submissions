class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCostMemo = {}

        def rec(i):
            if i>= len(cost):
                return 0
            if i in minCostMemo:
                return minCostMemo[i]
            minCostMemo[i] = cost[i] + min(rec(i+1), rec(i+2))
            return minCostMemo[i]

        return min(rec(0), rec(1))