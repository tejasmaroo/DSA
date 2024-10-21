class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        def check_palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        longest = ""
        for i in range(len(s)):
            palindromeOdd = check_palindrome(i, i)
            palindromeEven = check_palindrome(i, i + 1)

            if len(palindromeOdd) > len(longest):
                longest = palindromeOdd

            if len(palindromeEven) > len(longest):
                longest = palindromeEven
        
        return longest
