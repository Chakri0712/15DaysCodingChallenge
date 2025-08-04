# Last updated: 8/4/2025, 11:08:30 AM
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)