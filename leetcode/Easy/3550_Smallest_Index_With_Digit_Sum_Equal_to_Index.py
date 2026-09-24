"""
LeetCode 3550. Smallest Index With Digit Sum Equal to Index

Difficulty: Easy

Method 1: Digit Extraction

Approach:
- Traverse the array from left to right.
- For each number, calculate the sum of its digits.
- Compare the digit sum with the current index.
- Return the first index where both values are equal.
- If no such index exists, return -1.

Time Complexity: O(n × d)

Space Complexity: O(1)

where:
- n = number of elements
- d = number of digits in each number

Concepts:
- Array Traversal
- Digit Extraction
- Digit Sum
- Modulo and Integer Division
"""

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):

            digit_sum = 0
            temp = nums[i]

            while temp > 0:
                digit_sum += temp % 10
                temp //= 10

            if digit_sum == i:
                return i

        return -1
