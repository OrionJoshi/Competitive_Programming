# Method-1 Brute Force approach

def gridTraversal(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTraversal(m - 1, n) + gridTraversal(m, n - 1)

# Time Complexity : O(2^(m + n))
# Space Complexity : O(n + m)