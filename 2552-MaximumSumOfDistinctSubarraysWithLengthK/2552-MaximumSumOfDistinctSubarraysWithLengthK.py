# Last updated: 02/08/2025, 14:42:22
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = max_sum = window_sum = 0
        count = {}
        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1
            window_sum += nums[right]

            if right-left+1 > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                window_sum -= nums[left]
                left +=1

            if right -left+1 == k and len(count) == k:
                max_sum = max(max_sum, window_sum)
        return max_sum


        