"""
LeetCode 1189. Maximum Number of Balloons

Difficulty: Easy

Method 1: Frequency Hash Map

Approach:
- Count the frequency of every character in the string.
- Extract the counts of the letters required to form "balloon".
- Since 'l' and 'o' appear twice in "balloon",
  divide their frequencies by 2.
- The minimum frequency among all required letters
  determines the maximum number of times "balloon"
  can be formed.

Time Complexity: O(n)

Space Complexity: O(1)

Concepts:
- Hash Map
- Frequency Counting
- String Processing
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        freq = {}

        for ch in text:
            freq[ch] = freq.get(ch, 0) + 1

        b = freq.get('b', 0)
        a = freq.get('a', 0)
        l = freq.get('l', 0) // 2
        o = freq.get('o', 0) // 2
        n = freq.get('n', 0)

        return min(b, a, l, o, n)



# from collections import Counter

# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:

#         freq = Counter(text)

#         return min(
#             freq['b'],
#             freq['a'],
#             freq['l'] // 2,
#             freq['o'] // 2,
#             freq['n']
#         )
