# Last updated: 8/4/2025, 4:03:40 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = defaultdict(list)
        n = len(strs)
        if n==1:
            return [strs]
        for word in strs:
            sorted_word = ''.join(sorted(word))
            output_dict[sorted_word].append(word)
        return list(output_dict.values())
