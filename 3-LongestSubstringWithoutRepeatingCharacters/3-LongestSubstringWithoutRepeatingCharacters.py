# Last updated: 02/08/2025, 14:42:45
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_map = {}
        max_len = 0
        for right in range(len(s)):
            char = s[right]

            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1

            char_map[char] = right

            max_len = max(max_len, right-left+1)

        return max_len
        