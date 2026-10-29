"""
LeetCode 49. Group Anagrams

Difficulty: Medium

Method 1: Hash Map + Sorting

Approach:
- Create a dictionary to group anagrams.
- Sort each word's characters to generate a common key.
- Words that are anagrams have the same sorted key.
- Append each word to its corresponding group.
- Return all groups as a list.

Time Complexity: O(n * k log k)

Space Complexity: O(n * k)

where:
- n = number of strings
- k = maximum length of a string

Concepts:
- Hash Map
- Sorting
- String Processing
- Grouping
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            groups[key] = groups.get(key, [])
            groups[key].append(word)

        return list(groups.values())
