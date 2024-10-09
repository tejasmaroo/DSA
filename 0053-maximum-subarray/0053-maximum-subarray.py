class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        result = float('-inf')
        curr_sum = 0
        for i in nums:
            curr_sum += i
            result = max(result, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return result