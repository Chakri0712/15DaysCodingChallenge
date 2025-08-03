# Last updated: 8/3/2025, 1:47:32 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #  Brute force
        # import math
        # prod_arr = []
        # for i in range(len(nums)):
        #     sliced_arr = nums[:i]+nums[i+1:]
        #     prod_arr.append(math.prod(sliced_arr))
        # return prod_arr

        n = len(nums)
        prod_arr = [1]*n
        prefix_product = suffix_product = 1
        # first pass ----------- calculate prefix product
        for i in range(n):
            prod_arr[i] = prefix_product
            prefix_product *= nums[i]

        # second pass --------- calculate suffix product
        for i in range(n-1, -1, -1):
            prod_arr[i]*=suffix_product
            suffix_product *= nums[i]

        return prod_arr


