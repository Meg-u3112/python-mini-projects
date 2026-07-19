"""
LeetCode 3689. Maximum Total Value of Chosen Subarrays

Difficulty: Easy

Method 1: Mathematical Observation

Approach:
- Find the maximum element in the array.
- Find the minimum element in the array.
- The highest possible value of any subarray is
  max(nums) - min(nums).
- Since the same subarray can be chosen multiple times,
  choose this optimal subarray exactly k times.

Time Complexity: O(n)

Space Complexity: O(1)

Concepts:
- Mathematics
- Greedy Observation
- Arrays
"""

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        best = max(nums) - min(nums)

        return best * k
