class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posNums = []
        negNums = []

        n = len(nums)

        for i in nums:
            if i > 0:
                posNums.append(i)
            if i < 0:
                negNums.append(i)

        print("Positive Numbers:", posNums)
        print("Negative Numbers:", negNums)

        res = []

        for i in range(min(len(posNums), len(negNums))):
            res.append(posNums[i])   
            res.append(negNums[i])   

        if len(posNums) > len(negNums):
            res.extend(posNums[len(negNums):])
        elif len(negNums) > len(posNums):
            res.extend(negNums[len(posNums):])
        return res