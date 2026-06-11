"""
LeetCode 53. Maximum Subarray

Difficulty: Medium

Method 1: Kadane's Algorithm (Optimal)

Approach:
- Keep track of the maximum subarray ending at the current index.
- Either:
    1. Start a new subarray from the current element.
    2. Extend the previous subarray.
- Update the global maximum at each step.

Time Complexity: O(n)
Space Complexity: O(1)

Concepts:
- Dynamic Programming
- Kadane's Algorithm
- Array Traversal
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum


"""
Method 2: Brute Force

Approach:
- Generate every possible subarray.
- Compute its sum.
- Track the maximum sum.

Time Complexity: O(n²)
Space Complexity: O(1)

Concepts:
- Nested Loops
- Subarray Enumeration
"""

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#
#         ans = nums[0]
#
#         for i in range(len(nums)):
#             curr_sum = 0
#
#             for j in range(i, len(nums)):
#                 curr_sum += nums[j]
#                 ans = max(ans, curr_sum)
#
#         return ans
