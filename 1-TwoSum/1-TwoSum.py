# Last updated: 02/08/2025, 14:42:46
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen_dict:
                return [seen_dict[diff], i]
            seen_dict[num]=i