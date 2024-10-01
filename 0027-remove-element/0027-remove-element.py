class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i, v in enumerate(nums):
            if v != val:
                nums[j] = v
                j += 1
        
        return j