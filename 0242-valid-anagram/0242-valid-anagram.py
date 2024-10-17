class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = [0] * 26
        count_t = [0] * 26
        
        # Fill frequency arrays
        for char in s:
            count_s[ord(char) - ord('a')] += 1
        
        for char in t:
            count_t[ord(char) - ord('a')] += 1
        
        # Compare the two frequency arrays
        return count_s == count_t