# Last updated: 8/20/2025, 6:13:01 PM
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        low,high=0,x
        while low <= high:
            mid = low + (high-low)//2
            if mid*mid == x:
                return mid
            if mid*mid > x:
                high = mid-1
            elif mid*mid < x:
                low=mid+1
        return low-1

        