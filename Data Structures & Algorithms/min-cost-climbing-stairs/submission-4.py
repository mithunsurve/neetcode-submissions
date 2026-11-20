class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def rec(n):
            if n in memo:
                return memo[n]
            if n>=len(cost):
                return 0
            memo[n] = min(cost[n] + rec(n+1), cost[n] + rec(n+2))
            return memo[n]

        return min(rec(0), rec(1))

            