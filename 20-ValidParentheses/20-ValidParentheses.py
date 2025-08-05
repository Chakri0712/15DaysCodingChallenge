# Last updated: 8/5/2025, 11:44:09 AM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranthesis = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in paranthesis.values():
                stack.append(char)
            elif char in paranthesis:
                if not stack:
                    return False
                top_element = stack.pop()
                if paranthesis[char] != top_element:
                    return False
        return not stack

        