# Two Sum II - Input Array is Sorted

## Problem
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Return the indices of the two numbers as an array.

## Solution Approach: Two Pointers

Since the array is sorted, we can use the two-pointer technique to efficiently find the target sum.

### Algorithm
1. Initialize two pointers: `left` at index 0 and `right` at the last index
2. Calculate the sum of elements at both pointers
3. If sum equals target: return the 1-indexed positions
4. If sum is less than target: move left pointer right (increase sum)
5. If sum is greater than target: move right pointer left (decrease sum)
6. Repeat until we find the target sum

### Example
```
numbers = [2, 7, 11, 15], target = 9

Step 1: l=0, r=3 → 2+15=17 > 9 → move r left
Step 2: l=0, r=2 → 2+11=13 > 9 → move r left  
Step 3: l=0, r=1 → 2+7=9 = 9 → found! return [1,2]
```

### Time & Space Complexity
- **Time Complexity**: O(n) - single pass through array
- **Space Complexity**: O(1) - only using two pointers

### Why This Works
The sorted property ensures that:
- Moving left pointer right always increases the sum
- Moving right pointer left always decreases the sum
- This guarantees we'll find the solution if it exists
