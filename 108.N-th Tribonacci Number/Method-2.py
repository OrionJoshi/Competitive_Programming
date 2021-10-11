# Method-2 memoization

def tribonacci(n, memo = {}):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    if n == 2:
        return 1
    memo[n] = tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo)
    return memo[n]

# Time Complexity : O(n)
# Space Complexity : O(n)