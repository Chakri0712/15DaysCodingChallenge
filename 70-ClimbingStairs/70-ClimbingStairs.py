# Last updated: 8/21/2025, 4:57:20 PM
class Solution:
    def __init__(self):
        self.cache= {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.cache[n]
        