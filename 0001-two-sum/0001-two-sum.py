class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[v] = i