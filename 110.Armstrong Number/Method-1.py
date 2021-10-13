# Method-1

def isArmstrong(num):

    length = len(str(num))
    result = 0
    tempNum = num
    
    while tempNum:

        result += (tempNum % 10) ** (length)
        tempNum //= 10
    
    return result == num

# Time Complexity : O(n)
# Space Complexity : O(1)

# Input: 153
# Output: true
# Explanation:
# 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.