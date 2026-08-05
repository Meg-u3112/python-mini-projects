"""
LeetCode 12. Integer to Roman

Difficulty: Medium

Method 1: Greedy

Approach:
- Store Roman numeral values and their corresponding symbols
  in descending order.
- Traverse the values from largest to smallest.
- While the current value can be subtracted from the number:
    - Append its Roman symbol.
    - Reduce the number.
- Continue until the number becomes 0.

Time Complexity: O(1)

Space Complexity: O(1)

Concepts:
- Greedy Algorithm
- String Construction
- Mapping
"""

class Solution:
    def intToRoman(self, num: int) -> str:

        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        answer = ""

        for i in range(len(values)):

            while num >= values[i]:
                answer += symbols[i]
                num -= values[i]

        return answer
