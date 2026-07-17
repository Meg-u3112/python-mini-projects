"""
LeetCode 1672. Richest Customer Wealth

Difficulty: Easy

Method 1: Row Sum

Approach:
- Traverse each customer's bank accounts.
- Compute the total wealth using sum().
- Keep track of the maximum wealth encountered.
- Return the maximum wealth.

Time Complexity: O(m × n)

Space Complexity: O(1)

where:
m = number of customers
n = number of bank accounts per customer

Concepts:
- 2D Array
- Array Traversal
- Row Sum
- Maximum Value
"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        maximum = 0

        for row in accounts:
            total = sum(row)
            maximum = max(maximum, total)

        return maximum
