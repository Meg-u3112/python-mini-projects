"""
LeetCode 3789. Minimum Cost to Acquire Required Items

Difficulty: Medium

Method 1: Greedy Approach (Compare Three Strategies)

Approach:
- Calculate the cost of purchasing all items individually.
- Calculate the cost of purchasing only combined items.
- Calculate the cost of purchasing combined items first,
  then individual items for the remaining requirements.
- Compare the three possible costs and return the minimum.

Time Complexity: O(1)

Auxiliary Space Complexity: O(1)

Concepts:
- Greedy Approach
- Mathematical Optimization
- Minimum Cost
- min() and max()
"""

class Solution:
    def minimumCost(self, cost1: int, cost2: int,
                    costBoth: int, need1: int, need2: int) -> int:

        # Strategy 1: Buy individual items
        a = need1 * cost1 + need2 * cost2

        # Strategy 2: Buy only combined items
        b = max(need1, need2) * costBoth

        # Strategy 3: Buy combined items first
        mn = min(need1, need2)

        c = (mn * costBoth
             + (need1 - mn) * cost1
             + (need2 - mn) * cost2)

        return min(a, b, c)
