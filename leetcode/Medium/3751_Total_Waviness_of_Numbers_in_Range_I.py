"""
LeetCode 3751. Total Waviness of Numbers in Range I

Difficulty: Medium

Approach:
- Iterate through every number in the range [num1, num2].
- Convert each number to a string.
- For each digit except the first and last:
    - Count it as a peak if it is greater than both neighbors.
    - Count it as a valley if it is less than both neighbors.
- Sum the waviness of all numbers.

Time Complexity:
O((num2 - num1 + 1) * d)

Space Complexity:
O(d)

Concepts:
- String Processing
- Simulation
- Peak Detection
- Valley Detection
"""
