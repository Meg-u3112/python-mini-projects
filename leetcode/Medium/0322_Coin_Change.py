"""
LeetCode 322. Coin Change

Difficulty: Medium

Method 1: Dynamic Programming (Bottom-Up)

Approach:
- Create a DP array where dp[i] represents the minimum
  number of coins needed to make amount i.
- Initialize dp[0] = 0 because no coins are needed
  to make amount 0.
- For every amount from 1 to target:
    - Try every coin.
    - If the coin can contribute to the current amount,
      update dp[i] using:
          dp[i] = min(dp[i], dp[i - coin] + 1)
- If dp[amount] remains infinity, return -1.
- Otherwise, return dp[amount].

Time Complexity: O(amount × number_of_coins)

Space Complexity: O(amount)

Concepts:
- Dynamic Programming
- Bottom-Up DP
- Unbounded Knapsack
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):

            for coin in coins:

                if coin <= i:
                    dp[i] = min(
                        dp[i],
                        dp[i - coin] + 1
                    )

        if dp[amount] == float("inf"):
            return -1

        return dp[amount]
