# Method-1

def PredictTheWinner(nums):
      dp = [[0] * len(nums) for _ in range(len(nums))]

      for s in range(len(nums)):
          for i in range(len(nums)-s):
              j = i + s
              if i == j:
                  dp[i][i] = nums[i]
              else:
                  dp[i][j] = max(nums[j] - dp[i][j-1], nums[i] - dp[i+1][j])

      return dp[0][-1] >= 0

# Time Complexity : O(n^2)
# Space Complexity : O(n)