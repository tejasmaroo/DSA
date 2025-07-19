# Container With Most Water

## Problem
Given `n` non-negative integers `height[0], height[1], ..., height[n-1]` representing an elevation map where the width of each bar is 1, find two lines that together with the x-axis form a container that can hold the most water.

## Solution Approach: Two Pointers

Use two pointers starting from both ends of the array to find the maximum water area.

### Algorithm
1. Initialize two pointers: `left` at index 0 and `right` at the last index
2. Calculate the current area: `area = (right - left) * min(height[left], height[right])`
3. Update maximum area if current area is larger
4. Move the pointer with the smaller height inward:
   - If `height[left] < height[right]`: move left pointer right
   - Otherwise: move right pointer left
5. Repeat until pointers meet

### Example
```
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

Step 1: l=0, r=8 → area = 8 * min(1,7) = 8 * 1 = 8, move l (smaller height)
Step 2: l=1, r=8 → area = 7 * min(8,7) = 7 * 7 = 49, move r (smaller height)
Step 3: l=1, r=7 → area = 6 * min(8,3) = 6 * 3 = 18, move r (smaller height)
...continue until l >= r

Maximum area found: 49
```

### Key Insight
**Why move the pointer with smaller height?**
- The area is limited by the shorter line: `min(height[left], height[right])`
- Moving the pointer with the taller height will only decrease the width without potential for increasing the limiting height
- Moving the pointer with the shorter height gives us a chance to find a taller line

### Visualization
```
Container formed by lines at positions i and j:
Width = j - i
Height = min(height[i], height[j])
Area = Width × Height
```

### Time & Space Complexity
- **Time Complexity**: O(n) - single pass with two pointers
- **Space Complexity**: O(1) - only using constant extra space

### Why This Works
1. We start with the maximum possible width
2. As we move inward, width decreases, so we need to find taller heights to maximize area
3. Moving the shorter pointer gives us the best chance to find a configuration with larger area
4. This greedy approach ensures we don't miss the optimal solution
