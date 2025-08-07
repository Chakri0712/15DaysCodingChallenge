# Last updated: 8/7/2025, 11:56:06 AM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low,high=0,n-1
        while low <= high:
            mid = low + (high-low) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
        return low
        