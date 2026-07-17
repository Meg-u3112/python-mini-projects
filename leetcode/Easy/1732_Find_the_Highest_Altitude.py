"""
LeetCode 1732. Find the Highest Altitude

Difficulty: Easy

Method 1: Prefix Sum

Approach:
- The biker starts at altitude 0.
- Traverse the gain array and maintain the current altitude.
- Update the highest altitude after each step.
- Return the maximum altitude reached.

Time Complexity: O(n)

Space Complexity: O(1)

Concepts:
- Prefix Sum
- Array Traversal
- Running Sum
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        current = 0
        highest = 0

        for num in gain:
            current += num
            highest = max(highest, current)

        return highest
