"""
LeetCode 1385. Find the Distance Value Between Two Arrays

Difficulty: Easy

Method 1: Brute Force + all()

Approach:
- Iterate through each element in arr1.
- Check whether its absolute difference from every element in arr2
  is greater than d.
- If all differences are greater than d, increment the count.
- Return the final count.

Time Complexity: O(n * m)

Space Complexity: O(1)

where:
- n = length of arr1
- m = length of arr2

Concepts:
- Nested Loops
- Absolute Difference
- all() Function
- Array Traversal
"""

class Solution:
    def findTheDistanceValue(
        self, arr1: List[int], arr2: List[int], d: int
    ) -> int:

        initial = 0

        for num1 in arr1:
            if all(abs(num1 - num2) > d for num2 in arr2):
                initial += 1

        return initial
