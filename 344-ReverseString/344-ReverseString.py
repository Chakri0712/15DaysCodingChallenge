# Last updated: 02/08/2025, 14:42:33
class Solution(object):
    def reverseString(self, s):
        a = 0
        b = len(s)-1
        temp = ""
        while a<b:
            temp = s[a]
            s[a] = s[b]
            s[b] = temp
            a+=1
            b-=1
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        