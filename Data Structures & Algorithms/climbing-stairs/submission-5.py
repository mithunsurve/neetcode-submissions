class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        curr = 2
        prev = 1
        for _ in range(3, n+1):
            prev, curr = curr, prev + curr

        return curr