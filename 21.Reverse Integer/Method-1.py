# Method-1 

def reverseInt(n):
    isNegative = True if n < 0 else False
    positiveNum = abs(n)
    
    reverseNum = 0
    while positiveNum:
        rem = positiveNum % 10
        reverseNum = reverseNum * 10 + rem
        positiveNum = int(positiveNum / 10)
    if isNegative:
        reverseNum = -1 * reverseNum
        
    if reverseNum >= pow(2, 31) - 1 or reverseNum <= - pow(2, 31):
        return 0
    else:
        return reverseNum
    
# Time Complexity : O(logn)
# Space Complexity : O(1)