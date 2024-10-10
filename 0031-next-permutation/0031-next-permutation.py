class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1 Find the Pivot
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        # special case: if the whole list is in decreasing order then return the sorted nums
        if i == -1:
            return nums.sort()

        # Step 2 Find the righmost successor 
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1 

        # Step 3 Swap the Pivot and Successor
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4 Reverse the Suffix
        nums[i + 1:] = reversed(nums[i + 1:])
        return nums