"""
LeetCode 300. Longest Increasing Subsequence

Difficulty: Medium

Method 1: Dynamic Programming

Approach:
- Let dp[i] represent the length of the longest increasing
  subsequence ending at index i.
- Initialize every dp[i] as 1 since every element itself
  forms an increasing subsequence.
- For every index i, check all previous indices j.
- If nums[j] < nums[i], update dp[i] using dp[j] + 1.
- Return the maximum value in dp.

Time Complexity: O(n²)

Space Complexity: O(n)

Concepts:
- Dynamic Programming
- Arrays
- Longest Increasing Subsequence
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
