"""
LeetCode 628. Maximum Product of Three Numbers

Difficulty: Easy

Method 1: Sorting

Approach:
- Sort the array in ascending order.
- Compute the product of the three largest numbers.
- Compute the product of the two smallest numbers and the largest number.
- Return the maximum of the two products.

Time Complexity: O(n log n)

Space Complexity: O(1) (excluding sorting)

Concepts:
- Sorting
- Arrays
- Greedy Observation
- Negative Numbers
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        nums.sort()

        product1 = nums[-1] * nums[-2] * nums[-3]
        product2 = nums[0] * nums[1] * nums[-1]

        return max(product1, product2)
