class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        prev = 1
        curr = 2
        for i in range(2, n):
            tmp = prev + curr
            prev = curr
            curr = tmp
        
        return curr

            
