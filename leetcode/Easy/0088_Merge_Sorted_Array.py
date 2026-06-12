"""
LeetCode 88. Merge Sorted Array

Difficulty: Easy

Method 1: Three Pointers (Optimal)

Approach:
- Since nums1 has extra space at the end, merge from the back.
- Compare the largest remaining elements in nums1 and nums2.
- Place the larger element at the end of nums1.
- Continue until all elements from nums2 are processed.

Time Complexity: O(m + n)
Space Complexity: O(1)

Concepts:
- Two Pointers
- Array Manipulation
- In-place Merging
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int,
              nums2: List[int], n: int) -> None:

        i = m - 1      # Last valid element in nums1
        j = n - 1      # Last element in nums2
        k = m + n - 1  # Last position in nums1

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


"""
Method 2: Sort After Merge

Approach:
- Copy nums2 into the empty slots of nums1.
- Sort nums1.

Time Complexity: O((m+n) log(m+n))
Space Complexity: O(1)

Concepts:
- Sorting
- Array Manipulation
"""

# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         nums1[m:] = nums2
#         nums1.sort()
