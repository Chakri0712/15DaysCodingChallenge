# Last updated: 8/7/2025, 2:27:04 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        low,high,sum=0,n-1,0
        while low<=high:
            sum = numbers[low]+numbers[high]
            if target == sum:
                return [low+1, high+1]
            if sum > target:
                high -=1
            elif sum < target:
                low+=1
        
        return [0,0]