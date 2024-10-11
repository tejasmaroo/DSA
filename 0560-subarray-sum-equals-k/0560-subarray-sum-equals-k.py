class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cum_sum = 0
        sum_map = {0: 1}  # Initialize with 0 sum seen once to handle subarrays starting from the beginning
        
        for num in nums:
            cum_sum += num
            
            # Check if (cum_sum - k) exists in sum_map
            if cum_sum - k in sum_map:
                count += sum_map[cum_sum - k]
            
            # Update sum_map with the current cumulative sum
            if cum_sum in sum_map:
                sum_map[cum_sum] += 1
            else:
                sum_map[cum_sum] = 1
        
        return count