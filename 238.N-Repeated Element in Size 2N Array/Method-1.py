# Method-1

def repeatedNTimes(nums):

    uniqueItem = set(nums)
    diffSum = sum(nums) - sum(uniqueItem)
    diffLen = len(nums) - len(uniqueItem)
    
    return diffSum // diffLen

# Time Complexity : O(n)
# Space Complexity : O(n)