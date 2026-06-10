"""
LeetCode 242. Valid Anagram

Difficulty: Easy

Method 1: Frequency Hash Map

Approach:
- If the lengths are different, they cannot be anagrams.
- Count the frequency of each character in both strings.
- Compare the two frequency maps.
- If they are equal, the strings are anagrams.

Time Complexity: O(n)
Space Complexity: O(1)

Concepts:
- Hash Map
- Frequency Counting
- String Processing
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq_l = {}
        freq_r = {}

        for ch in s:
            freq_l[ch] = freq_l.get(ch, 0) + 1

        for ch in t:
            freq_r[ch] = freq_r.get(ch, 0) + 1

        return freq_l == freq_r


"""
Method 2: Counter

Approach:
- Use Python's built-in Counter to count character frequencies.
- Compare the two Counter objects directly.

Time Complexity: O(n)
Space Complexity: O(1)

Concepts:
- Counter
- Hash Map
- Frequency Counting
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
