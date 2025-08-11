# Last updated: 8/11/2025, 4:11:26 PM
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(s)
        m=len(p)
        left=0
        result = []

        if m > n:
            return result

        p_counts = Counter(p)
        s_window_counts = Counter(s[:m])

        if p_counts == s_window_counts:
            result.append(0)

        for right in range(m, n):
            s_window_counts[s[right]] += 1 # Add the next element
            s_window_counts[s[right-m]] -= 1 # remove the leaving element

            if s_window_counts == p_counts:
                result.append(right-m+1)
        return result