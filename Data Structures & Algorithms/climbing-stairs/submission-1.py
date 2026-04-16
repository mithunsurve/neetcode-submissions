class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        return self.climb(n, memo)

    def climb(self,n, memo):
        if n in memo:
            return memo[n]

        if n==1 or n==2 or n==0:
            return n

        result = self.climb(n-1, memo) + self.climb(n-2, memo)

        memo[n]=result

        return result