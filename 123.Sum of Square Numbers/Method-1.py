# Method-1

def judgeSquareSum(c):
    if c == 1:
        return True
    left = 0
    right = int(c * 0.5)

    while left <= right:
        sqrSum = left ** 2 + right ** 2
        if sqrSum == c:
            return True
        elif sqrSum < c:
            left += 1
        else:
            right -= 1

    return False

# Time Complexity : O(sqrt(c))
# Space Complexity : O(1)