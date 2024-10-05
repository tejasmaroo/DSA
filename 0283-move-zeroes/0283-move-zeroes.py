class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        flag = 0
        if len(nums) == 1:
            nums = nums
        while flag <= zero_count:
            for i in range(len(nums)):
                if nums[i] == 0 and i + 1 != len(nums):
                    t = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = t
            flag += 1
            