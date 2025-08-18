# Last updated: 8/18/2025, 9:22:54 AM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result = []

        for fixed in range(n-2):
            if fixed > 0 and nums[fixed] == nums[fixed-1]:
                continue
            left=fixed+1
            right= n-1
            while left < right:
                sum=nums[fixed]+nums[left]+nums[right]
                if sum == 0:
                    result.append([nums[fixed],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif sum > 0:
                    right-=1
                else:
                    left+=1
        return result

            
        