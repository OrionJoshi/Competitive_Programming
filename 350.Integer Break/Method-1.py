# Method-1

def integerBreak(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
            
    return dp[n]

# Time Complexity : O(n^2)
# Space Complexity : O(n)