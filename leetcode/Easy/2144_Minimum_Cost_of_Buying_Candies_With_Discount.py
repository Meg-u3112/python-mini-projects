"""
LeetCode 2144. Minimum Cost of Buying Candies With Discount

Difficulty: Easy

Approach:
1. Sort candies in descending order.
2. Every third candy becomes free.
3. Add all candies except every third candy.

Time Complexity: O(n log n)
Space Complexity: O(1)

Concepts:
- Sorting
- Greedy
"""

class Solution:
    def minimumCost(self, cost):
        cost.sort(reverse=True)

        total = 0

        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                total += cost[i]

        return total
