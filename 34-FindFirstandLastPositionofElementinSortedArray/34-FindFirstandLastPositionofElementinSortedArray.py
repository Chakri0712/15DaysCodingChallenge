# Last updated: 06/08/2025, 23:39:43
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        if n == 0:
            return [-1, -1]
        low,high=0,n-1
        first_occurance=last_occurance = -1
        while low <= high:
            mid = low + (high-low) // 2
            if target == nums[mid]:
                first_occurance = mid
                high = mid-1
            elif target<nums[mid]:
                high = mid-1
            elif target > nums[mid]:
                low = mid+1
            
        if first_occurance == -1:
            return [first_occurance,last_occurance]
            
        low,high=0,n-1
        while low <= high:
            mid = low + (high-low) // 2
            if target == nums[mid]:
                last_occurance = mid
                low=mid+1
            elif target<nums[mid]:
                high = mid-1
            elif target > nums[mid]:
                low = mid+1

        return [first_occurance,last_occurance]

