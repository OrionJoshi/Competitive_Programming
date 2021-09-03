# Method-1 Using Mathematical approach

def addDigits(num):
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9

# Time Complexity : O(1)
# Space Complexity : O(1)