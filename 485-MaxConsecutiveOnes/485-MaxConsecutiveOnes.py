# Last updated: 8/18/2025, 9:22:27 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        max_count=curr_count=0
        for right in range(n):
            if nums[right] == 1:
                curr_count +=1
                max_count = max(curr_count, max_count)
            else:
                curr_count = 0
        return max_count
        