class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, one_count = 0, 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                one_count = max(one_count, count)
                count = 0
        return max(one_count, count)