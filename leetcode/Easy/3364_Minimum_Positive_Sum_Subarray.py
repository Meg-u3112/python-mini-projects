"""
LeetCode 3364. Minimum Positive Sum Subarray

Difficulty: Easy

Method 1: Brute Force (Nested Loops)

Approach:
- Initialize the answer with infinity to track the minimum
  positive subarray sum.
- Traverse the array using an outer loop to select the
  starting index.
- Use an inner loop to select the ending index.
- Calculate the subarray length.
- Check whether the subarray length is between l and r.
- Calculate the subarray sum and check if it is positive.
- Update the answer with the minimum positive sum.
- Return -1 if no valid positive subarray exists.

Time Complexity: O(n^3)
- Nested loops take O(n^2).
- Calculating sum() for each subarray takes O(n).

Auxiliary Space Complexity: O(1)
(excluding temporary slicing)

Concepts:
- Brute Force
- Nested Loops
- Subarrays
- Array Traversal
- Minimum Value Tracking
- Conditional Filtering
"""

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        ans = float('inf')

        for i in range(len(nums)):
            for j in range(i, len(nums)):

                length = j - i + 1

                if l <= length <= r:
                    total = sum(nums[i:j+1])

                    if total > 0:
                        ans = min(ans, total)

        return -1 if ans == float('inf') else ans
