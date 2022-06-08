# Method-1

def divisorGame(n):
    dp = [False for i in range(n + 1)]
    for i in range(n + 1):
          for j in range(1, i//2 + 1):
                if i % j == 0 and (not dp[i - j]):
                    dp[i] = True
                    break
    return dp[n]

# Time Complexity : O(n^2)
# Space Complexity : O(n)