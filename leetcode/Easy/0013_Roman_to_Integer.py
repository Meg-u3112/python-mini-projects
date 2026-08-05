"""
LeetCode 13. Roman to Integer

Difficulty: Easy

Method 1: Greedy Traversal

Approach:
- Store the value of each Roman numeral in a hash map.
- Traverse the string from left to right.
- If the current numeral is smaller than the next numeral,
  subtract its value.
- Otherwise, add its value.
- The last character is always added.

Time Complexity: O(n)

Space Complexity: O(1)

Concepts:
- Hash Map
- String Traversal
- Greedy
"""

class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i in range(len(s)):

            current = roman[s[i]]

            if i < len(s) - 1:

                nxt = roman[s[i + 1]]

                if current < nxt:
                    total -= current
                else:
                    total += current

            else:
                total += current

        return total
