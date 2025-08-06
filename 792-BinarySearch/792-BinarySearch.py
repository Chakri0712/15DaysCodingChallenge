# Last updated: 8/6/2025, 4:44:59 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= len(nums)
        low,high=0,n-1
        while low <= high:
            mid = low + (high-low) // 2 # For larger inputs this is a better way of calculating mid
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid-1
            elif target > nums[mid]:
                low = mid+1
        return -1

        