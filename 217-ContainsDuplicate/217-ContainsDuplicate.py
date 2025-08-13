# Last updated: 8/13/2025, 6:22:42 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = set()
        for ele in nums:
            if ele in distinct:
                return True
            distinct.add(ele)
        return False        