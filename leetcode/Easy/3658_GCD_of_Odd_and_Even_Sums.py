"""
LeetCode 3658. GCD of Odd and Even Sums

Difficulty: Easy

Method 1: Brute Force

Approach:
- Compute the sum of the first n odd numbers.
- Compute the sum of the first n even numbers.
- Iterate from 1 to the smaller sum.
- Find the largest common divisor.

Time Complexity: O(n²)
Space Complexity: O(1)

Concepts:
- Simulation
- GCD
"""
"""
Method 2: Euclidean Algorithm

Approach:
- Compute both sums.
- Use Python's built-in gcd() function.

Time Complexity: O(log n)
Space Complexity: O(1)

Concepts:
- Mathematics
- Euclidean Algorithm
"""
from math import gcd

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        odd_total = n * n
        even_total = n * (n + 1)

        return gcd(odd_total, even_total)
"""
Method 3: Mathematical Observation (Optimal)

Observation:
sumOdd = n²
sumEven = n(n+1)

GCD(n², n(n+1))
= n × GCD(n, n+1)

Since consecutive integers are always coprime:

GCD(n, n+1) = 1

Therefore,

Answer = n

Time Complexity: O(1)
Space Complexity: O(1)

Concepts:
- Number Theory
- Mathematical Proof
"""
