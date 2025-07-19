# 3Sum

## Solution Approach: Sort + Two Pointers

We combine sorting with the two-pointer technique to efficiently find all unique triplets that sum to zero.

### Algorithm
1. **Sort the array** to enable two-pointer technique and handle duplicates easily
2. **Fix the first element** and use two pointers for the remaining two elements
3. For each fixed element `a`:
   - Skip duplicates for the first element
   - Use two pointers (`left`, `right`) to find pairs that sum to `-a`
   - If sum < 0: move left pointer right
   - If sum > 0: move right pointer left  
   - If sum == 0: add triplet to result and skip duplicates

### Example
```
nums = [-1, 0, 1, 2, -1, -4]

After sorting: [-4, -1, -1, 0, 1, 2]

i=0, a=-4: l=1, r=5 → -4+(-1)+2 = -3 ≠ 0 (no valid triplets)
i=1, a=-1: l=2, r=5 → -1+(-1)+2 = 0 ✓ → triplet [-1,-1,2]
           l=3, r=4 → -1+0+1 = 0 ✓ → triplet [-1,0,1]
i=2: skip (duplicate -1)
...continue until end
```

### Key Points
- **Sorting**: Enables two-pointer approach and easier duplicate handling
- **Duplicate Skipping**: 
  - Skip duplicate first elements: `if i > 0 and a == nums[i-1]: continue`
  - Skip duplicate left pointers after finding a valid triplet
- **Two Pointers**: Used to find the remaining two numbers efficiently

### Time & Space Complexity
- **Time Complexity**: O(n²) - O(n log n) for sorting + O(n²) for nested loops
- **Space Complexity**: O(1) - excluding the output array, only using constant extra space

### Why This Works
1. Sorting allows us to use two pointers effectively
2. For each fixed first element, the problem reduces to "Two Sum" on the remaining array
3. Skipping duplicates ensures we don't have repeated triplets in our result
