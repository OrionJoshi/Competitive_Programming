# Method-3 Using Recursion

def tribonacci(n):
    if n < 2:
        return n
    if n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

# Time Complexity : O(2 ^ n)
# Space Complexity : O(n)