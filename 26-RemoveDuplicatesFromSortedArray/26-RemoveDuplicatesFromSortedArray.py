# Last updated: 02/08/2025, 14:42:42
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,1
        while j<len(nums):
            if nums[i]<nums[j]:
                temp=nums[j]
                nums[i+1]=nums[j]
                nums[j]=temp
                i+=1
            j+=1
        return i+1
        
        