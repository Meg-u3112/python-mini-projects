"""
LeetCode 347. Top K Frequent Elements

Difficulty: Medium

Method 1: Hash Map + Sorting

Approach:
- Count the frequency of each number using a hash map.
- Sort the unique numbers by their frequencies in descending order.
- Return the first k numbers with the highest frequencies.

Time Complexity: O(n + m log m)

Space Complexity: O(m)

where:
- n = number of elements in nums
- m = number of unique elements in nums

Concepts:
- Hash Map
- Frequency Counting
- Sorting
- Lambda / Key Function
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_nums = sorted(freq, key=freq.get, reverse=True)

        return sorted_nums[:k]
