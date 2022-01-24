# Method-1 In-place

def findDisappearedNumbers(nums):
    result = []
    
    for i in range(1, len(nums) + 1):
        currIdx = abs(nums[i - 1])
        if nums[currIdx - 1] > 0:
            nums[currIdx - 1] *= -1
            
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)
            
    return result

# Time Complexity : O(n)
# Space Complexity : O(1)