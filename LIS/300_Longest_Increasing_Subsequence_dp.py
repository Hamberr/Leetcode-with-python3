"""
Dynamic programming:
Creat list dp = [1] * len(nums) to store the present longest increasing subquences: dp[i] is the LIS of nums[0 : i], update dp[i] with dp[i] = max(dp[i], dp[j] + 1 for j in range(i) if nums[j] < nums[i];
Finally, return max(dp[i])
"""

class Solution:
    def lengthOfLIS(self, nums):

        if len(nums) <= 1:
            return len(nums)

        dp = len(nums) * [1]
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])

        return res
