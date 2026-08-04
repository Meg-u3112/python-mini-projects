"""
LeetCode 198. House Robber

Difficulty: Medium

Method 1: Dynamic Programming (Space Optimized)

Approach:
- At each house, we have two choices:
    1. Skip the current house.
    2. Rob the current house and add its value to the best
       result from two houses back.
- Maintain only the previous two DP states instead of
  storing the entire DP array.

Time Complexity: O(n)

Space Complexity: O(1)

Concepts:
- Dynamic Programming
- Space Optimization
- State Transition
"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):

            current = max(
                prev1,
                nums[i] + prev2
            )

            prev2 = prev1
            prev1 = current

        return prev1
