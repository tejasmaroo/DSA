class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        s_index = 0
        count = 0
        for c in t:
            if s_index < s_len and c == s[s_index]:
                s_index += 1

        if s_index == s_len:
            return True
        else:
            return False