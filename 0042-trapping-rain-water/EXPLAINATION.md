# Trapping Rain Water

## Problem
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Solution Approach: Two Pointers

Use two pointers with tracked maximum heights to calculate trapped water efficiently.

### Algorithm
1. Initialize two pointers: `left` at index 0 and `right` at the last index
2. Keep track of `leftMax` and `rightMax` (maximum heights seen so far from each side)
3. Move the pointer with the smaller maximum height:
   - If `leftMax < rightMax`: move left pointer and process left side
   - Otherwise: move right pointer and process right side
4. For the side being processed:
   - Update the respective max height
   - Add trapped water: `max_height - current_height`
5. Continue until pointers meet

### Example
```
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

Visual representation:
    3 |       ▓
    2 |   ▓ ~ ▓ ▓ ~ ▓
    1 | ▓ ~ ▓ ~ ▓ ~ ▓ ▓
    0 |▓▓▓▓▓▓▓▓▓▓▓▓
      0123456789AB

Water trapped (~ symbols): 6 units
```

### Key Insight
**Why does this work?**
- Water level at any position is determined by `min(leftMax, rightMax)`
- We only process the side with the smaller maximum because:
  - The water level is guaranteed to be at least that height
  - We don't need to know the exact other side's max, just that it's higher

### Step-by-Step Walkthrough
```
l=0, r=11, leftMax=0, rightMax=1
leftMax < rightMax → process left
l=1: leftMax=1, water=1-1=0

l=1, r=11, leftMax=1, rightMax=1  
leftMax == rightMax → process right
r=10: rightMax=2, water=2-2=0

...continue this process
```

### Time & Space Complexity
- **Time Complexity**: O(n) - single pass with two pointers
- **Space Complexity**: O(1) - only using constant extra space

### Alternative Approaches
1. **Brute Force**: O(n²) - for each position, find left and right max
2. **Dynamic Programming**: O(n) time, O(n) space - precompute left and right max arrays
3. **Two Pointers**: O(n) time, O(1) space - optimal solution

### Why This Works
1. Water trapped at position i = `min(leftMax[i], rightMax[i]) - height[i]`
2. We don't need to know both maxes exactly, just which side has the smaller max
3. By moving the pointer with smaller max, we ensure we're always calculating based on the correct limiting factor
