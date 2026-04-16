class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n ==0 or n==1 or n==2:
                return n

            memo[n]= dfs(n-1) + dfs(n-2)

            return memo[n]

        result = dfs(n)

        return result
            