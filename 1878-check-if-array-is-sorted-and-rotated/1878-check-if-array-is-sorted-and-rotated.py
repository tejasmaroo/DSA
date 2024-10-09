class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] > nums[i + 1]:
                count += 1
        return count <= 1 and (nums[-1] <= nums[0] or count == 0)