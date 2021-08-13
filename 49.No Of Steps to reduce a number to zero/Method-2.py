# Method-2

def numberOfSteps(num):
    if num == 0:
        return 0
        
    if num % 2 == 0:
        return 1 + numberOfSteps(num // 2)
    return 1 + numberOfSteps(num - 1)


# Time Complexity : O(logN)
# Space Complexity : O(logN)