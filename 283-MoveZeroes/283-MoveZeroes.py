# Last updated: 19/08/2025, 21:55:28
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        l=0
        for r in range(n):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l+=1
            r+=1
        