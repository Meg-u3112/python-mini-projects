"""
LeetCode 2161. Partition Array According to Given Pivot

Difficulty: Medium

Approach:
- Traverse the array once.
- Store numbers smaller than pivot in one list.
- Store numbers equal to pivot in another list.
- Store numbers greater than pivot in a third list.
- Concatenate the three lists.

Time Complexity: O(n)

Space Complexity: O(n)

Concepts:
- Arrays
- Partitioning
- Stable Ordering
"""

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        smaller = []
        equal = []
        greater = []

        for num in nums:

            if num < pivot:
                smaller.append(num)

            elif num == pivot:
                equal.append(num)

            else:
                greater.append(num)

        return smaller + equal + greater
