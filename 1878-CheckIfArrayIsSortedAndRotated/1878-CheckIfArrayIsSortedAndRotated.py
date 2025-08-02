# Last updated: 02/08/2025, 14:42:27
class Solution:
    def check(self, nums: List[int]) -> bool:
        i,j,break_point=0,1,0
        while j<=len(nums) and i<j:
            if j==len(nums):
                j=0
            if nums[i]>nums[j]:
                break_point+=1
            i+=1
            j+=1
        if break_point>1:
            return False
        return True
        