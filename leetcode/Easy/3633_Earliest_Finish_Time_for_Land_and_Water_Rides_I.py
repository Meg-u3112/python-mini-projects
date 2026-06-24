"""
Earliest Finish Time for Land and Water Rides I

Difficulty: Easy

Approach:
- Try every land ride and water ride pair.
- Consider both possible orders:
    1. Land -> Water
    2. Water -> Land
- Compute the finishing time for each order.
- Return the minimum finish time.

Time Complexity: O(n * m)

Space Complexity: O(1)

Concepts:
- Brute Force
- Simulation
- Scheduling
"""

class Solution:
    def earliestFinishTime(
        self,
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration
    ):

        ans = float("inf")

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                # Land -> Water
                land_finish = landStartTime[i] + landDuration[i]

                water_start = max(
                    land_finish,
                    waterStartTime[j]
                )

                finish1 = water_start + waterDuration[j]

                # Water -> Land
                water_finish = waterStartTime[j] + waterDuration[j]

                land_start = max(
                    water_finish,
                    landStartTime[i]
                )

                finish2 = land_start + landDuration[i]

                ans = min(ans, finish1, finish2)

        return ans
