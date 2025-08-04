# Last updated: 8/4/2025, 4:13:02 PM
class Solution:
    # using sorted method
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # using Counter
    # from collection import Counter
    # return Counter(s)==Counter(t)