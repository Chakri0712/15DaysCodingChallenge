# Last updated: 8/18/2025, 9:08:29 AM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            if digits[i] == 9:
                digits[i] = 0
            
        return [1] + digits
        