"""
LeetCode 3345. Smallest Divisible Digit Product I

Difficulty: Easy

Method 1: Brute Force

Approach:
- Start from the given number n.
- Compute the product of all digits of the current number.
- If the product is divisible by t, return the number.
- Otherwise, increment the number and repeat.

Time Complexity: O(k × d)

where:
- k = number of integers checked
- d = number of digits

Space Complexity: O(1)

Concepts:
- Brute Force
- Digit Extraction
- Modulo Arithmetic
"""

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:

            temp = n
            product = 1

            while temp > 0:
                product *= temp % 10
                temp //= 10

            if product % t == 0:
                return n

            n += 1
