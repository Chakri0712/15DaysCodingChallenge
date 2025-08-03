# Last updated: 8/3/2025, 1:10:28 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=max_profit=0
        for right in range(len(prices)):
            while prices[right] < prices[left]:
                left+=1
            curr_profit=prices[right]-prices[left]
            max_profit=max(curr_profit, max_profit)
            right+=1
        return max_profit

        