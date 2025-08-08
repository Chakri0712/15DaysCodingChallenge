# Last updated: 8/8/2025, 12:40:48 PM
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            curr = nums[mid]
            if curr == target or nums[left] == target or nums[right] == target:
                return True
            elif curr == nums[left] and curr == nums[right]:
                left += 1
                right -= 1
            elif curr >= nums[left]:
                # left side sorted
                if target < nums[left] or target > curr:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # right side sorted
                if target > nums[right] or target < curr:
                    right = mid - 1
                else:
                    left = mid + 1
            
        return False
