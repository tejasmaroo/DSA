class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        parr = []
        narr = []
        for i in nums:
            if i>0:
                parr.append(i)
            else:
                narr.append(i)
        i,k = 0,0
        while i<len(parr):
            nums[k],nums[k+1] = parr[i],narr[i]
            i += 1
            k += 2 
        return nums