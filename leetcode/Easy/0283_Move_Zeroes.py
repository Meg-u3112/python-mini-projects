"""
LeetCode 283. Move Zeroes

Difficulty: Easy

Method 1: Extra Array

Approach:
- Store all non-zero elements in a new list.
- Count how many zeros were removed.
- Append the required number of zeros.
- Copy the result back into nums.

Time Complexity: O(n)
Space Complexity: O(n)

Concepts:
- Array Traversal
- List Manipulation
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        value = []

        for num in nums:
            if num != 0:
                value.append(num)

        zeros = len(nums) - len(value)
        value += [0] * zeros

        nums[:] = value


"""
Method 2: Two Pointers (Optimal)

Approach:
- Maintain a pointer pointing to where the next non-zero element should go.
- Traverse the array once.
- Whenever a non-zero element is found, swap it with the current pointer.
- Move the pointer forward.

Time Complexity: O(n)
Space Complexity: O(1)

Concepts:
- Two Pointers
- In-place Array Manipulation
"""

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#
#         left = 0
#
#         for right in range(len(nums)):
#
#             if nums[right] != 0:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1
