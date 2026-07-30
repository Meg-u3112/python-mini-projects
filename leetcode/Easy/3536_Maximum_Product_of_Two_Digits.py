"""
LeetCode 3536. Maximum Product of Two Digits

Difficulty: Easy

Method 1: Brute Force

Approach:
- Extract all digits of the number.
- Compare the product of every pair of digits.
- Return the maximum product found.

Time Complexity: O(d²)

Space Complexity: O(d)

where d is the number of digits.

Concepts:
- Digit Extraction
- Brute Force
- Array Traversal
"""

class Solution:
    def maxProduct(self, n: int) -> int:

        digits = []

        while n > 0:
            digits.append(n % 10)
            n //= 10

        maximum = 0

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                maximum = max(maximum, digits[i] * digits[j])

        return maximum
