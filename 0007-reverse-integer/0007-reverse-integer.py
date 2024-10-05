class Solution:
    def reverse(self, x: int) -> int:
        number = 0
        if x < 0:
            number = int(str(x)[1:][::-1]) * -1
        else:    
            while x > 0:
                ld = x % 10
                number = (number * 10) + ld
                x = x // 10

        if number > 2 ** 31 - 1 or number < -2 ** 31:
            return 0
        return number