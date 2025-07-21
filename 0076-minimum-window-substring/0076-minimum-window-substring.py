class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        # 1. Count Target Characters
        countT = {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        window = {} # To store counts of characters in the current window
        
        have = 0 # Number of unique characters in window that match countT's requirements
        need = len(countT) # Total number of unique characters in t

        res = [-1, -1]
        resLen = float("infinity")
        
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            # Check if the current character contributes to satisfying the 'need'
            if char in countT and window[char] == countT[char]:
                have += 1
            
            # 4. Check Condition and Shrink
            while have == need:
                # Update our result
                current_window_length = r - l + 1
                if current_window_length < resLen:
                    resLen = current_window_length
                    res = [l, r]
                
                # Try to shrink the window from the left
                char_to_remove = s[l]
                window[char_to_remove] -= 1
                l += 1

                # If removing this character causes us to lose a 'needed' character
                if char_to_remove in countT and window[char_to_remove] < countT[char_to_remove]:
                    have -= 1
        
        # Return the result
        start, end = res
        return s[start : end + 1] if resLen != float("infinity") else ""
