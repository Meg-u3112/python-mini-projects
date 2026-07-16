"""
LeetCode - Sum and Multiply

Difficulty: Easy

Method 1: String Traversal

Approach:
- Traverse each digit of the number as a string.
- Ignore all zero digits.
- Form a new number x by concatenating the non-zero digits.
- Compute the sum of the digits in x.
- Return x * sum.

Time Complexity: O(d)

Space Complexity: O(d)

where d is the number of digits.

Concepts:
- String Processing
- Digit Manipulation
- Simulation
"""

class Solution:
    def sumAndMultiply(self, n: int) -> int:

        digit_sum = 0
        number = ""

        for ch in str(n):

            if ch != "0":
                digit_sum += int(ch)
                number += ch

        if number == "":
            return 0

        return int(number) * digit_sum
