"""
LeetCode 238. Product of Array Except Self

Difficulty: Medium

Method 1: Prefix and Suffix Products

Approach:
- Initialize the answer array with 1s.
- Traverse from left to right and store the product of
  all elements to the left of each index.
- Traverse from right to left and multiply each answer
  by the product of all elements to its right.
- Return the answer array.

Time Complexity: O(n)

Auxiliary Space Complexity: O(1)
(excluding the output array)

Concepts:
- Prefix Products
- Suffix Products
- Array Traversal
- In-place Optimization
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n

        # Left products
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        # Right products
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
