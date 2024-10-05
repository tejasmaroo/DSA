class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        else:
            n = 0
            y = x
            while x > 0:
                ld = x % 10
                n = (n * 10) + ld
                x = x // 10
            if n == y:
                return True
            else:
                return False