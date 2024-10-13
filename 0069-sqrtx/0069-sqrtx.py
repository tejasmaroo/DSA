class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        result = 0
        if x == 0 or x == 1:
            return x
        while l <= r:
            mid = l + (r - l) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                result = mid
                l = mid + 1
            else:
                r = mid - 1
        return result