# Method-2

def judgeSquareSum(c):
    endPoint = int(c * 0.5)
    for i in range(endPoint + 1):
        x = (c - (i ** 2)) ** 0.5
        if x == int(abs(x)):
            return True
    return False

# Time Complexity : O(sqrt(c))
# Space Complexity : O(1)