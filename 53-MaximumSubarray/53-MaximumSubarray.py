# Last updated: 02/08/2025, 15:26:01
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n= len(nums)
        if n==1:
            return nums[0]
        curr_sum=0
        max_sum=sum(nums)

        for i in range(n):
            curr_sum = curr_sum + nums[i]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
        