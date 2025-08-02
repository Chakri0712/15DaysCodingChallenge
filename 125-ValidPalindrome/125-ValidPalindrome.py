# Last updated: 02/08/2025, 14:42:39
class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed_str = ''.join(char.lower() for char in s if char.isalnum())
        l,r=0,len(trimmed_str)-1
        while l<r:
            if trimmed_str[l] != trimmed_str[r]:
                return False
            l+=1
            r-=1
        return True
        