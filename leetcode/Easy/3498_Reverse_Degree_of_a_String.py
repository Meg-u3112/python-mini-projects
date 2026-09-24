"""
LeetCode 3498. Reverse Degree of a String

Difficulty: Easy

Method 1: Character Position Calculation

Approach:
- Traverse the string from left to right.
- Calculate each character's position in the reversed alphabet:
    a = 26, b = 25, ..., z = 1
- Multiply the reverse alphabet value by the character's
  1-indexed position in the string.
- Add all products to get the reverse degree.

Time Complexity: O(n)

Space Complexity: O(1)

Concepts:
- String Traversal
- ASCII / ord()
- Character Position
- Mathematical Calculation
"""

class Solution:
    def reverseDegree(self, s: str) -> int:

        total = 0

        for i in range(len(s)):

            ch = s[i]

            reverse_value = 26 - (ord(ch) - ord('a'))

            total += reverse_value * (i + 1)

        return total
