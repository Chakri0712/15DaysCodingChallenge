# Last updated: 8/18/2025, 9:22:24 AM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        max_sum=curr_sum=sum(nums[:k])
        for i in range(k,n):
            curr_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, curr_sum)
        return max_sum/k