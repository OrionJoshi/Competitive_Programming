# Method-2 Memoization approach

def gridTraversal(m, n, memo = {}):
    key = str(m) + ',' + str(n)

    if key in memo:
        return memo[key]

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    memo[key] = gridTraversal(m - 1, n, memo) + gridTraversal(m , n - 1, memo)

    return memo[key]

# Time Complexity : O((m * n))
# Space Complexity : O(n + m)