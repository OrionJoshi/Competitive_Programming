# Method-2 Using Math

def missingNumber(nums):
    length = len(nums)
    realSum = 0
    tempSum = 0
    
    for i in range(length + 1):
        realSum += i
    
    for num in nums:
        tempSum += num
       
    return realSum - tempSum

# Time Complexity : O(n)
# Space Complexity : O(1)
