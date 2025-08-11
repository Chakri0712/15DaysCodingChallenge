# Last updated: 8/11/2025, 3:15:25 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        left=max_len=max_freq=0
        char_count = {}
        for right in range(n):
            char_count[s[right]] = char_count.get(s[right], 0)+1
            max_freq = max(max_freq, char_count[s[right]])
            curr_window_length = right - left + 1
            if curr_window_length - max_freq > k:
                char_count[s[left]] -= 1
                left+=1
            max_len = max(max_len, right-left+1)
        return max_len