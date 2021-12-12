# Method-2

def thirdMax(nums):

    firstMax = secondMax = thirdMax = -float('inf')
    
    for num in nums:
        if num in (firstMax, secondMax, thirdMax):
            continue
        if num > firstMax:
            firstMax, num = num, firstMax
        if num > secondMax:
            secondMax, num = num, secondMax
        if num > thirdMax:
            thirdMax, num = num, thirdMax
        
    return firstMax if thirdMax == -float('inf') else thirdMax

# Time Complexity : O(n)
# Space Complexity : O(1)