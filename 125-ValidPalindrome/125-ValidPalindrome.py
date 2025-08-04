# Last updated: 8/4/2025, 11:06:34 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)