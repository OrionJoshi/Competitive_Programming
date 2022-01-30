# Method-1

def trailingZeroes(n):
    if n < 5:
        return 0
    x = 0
    while n != 0:
        x += n // 5
        n //= 5

    return x

# Time Complexity : O(log5(n))
# Space Complexity : O(1)