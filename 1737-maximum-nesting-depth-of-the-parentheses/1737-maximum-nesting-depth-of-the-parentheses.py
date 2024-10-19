class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxDepth = 0
        for char in s:
            if char == '(':
                count += 1
                maxDepth = max(count, maxDepth)
            elif char == ')':
                count -= 1
        return maxDepth