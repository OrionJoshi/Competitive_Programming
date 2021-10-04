# Method-1

def findErrorNums(nums):
    actualLen = len(nums)
    noDuplicateLen = len(set(nums))
    
    if actualLen == noDuplicateLen:
        return False
    else:
        return True

# Time Complexity : O(n)
# Space Complexity : O(1)

# Input: nums = [1,2,3,1]
# Output: true