class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        firstPos = -1
        lastPos = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                firstPos = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if firstPos == -1:
            return [-1, -1]
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                lastPos = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return [firstPos, lastPos]