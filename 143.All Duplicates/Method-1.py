# Method-1 

def findDuplicates(nums):
    length = len(nums)
    result = []
    
    for i in range(0, length):
        if nums[abs(nums[i]) - 1] > 0:
            nums[abs(nums[i]) - 1] *= -1
        else:
            result.append(abs(nums[i]))
    return result

# Time Complexity : O(n)
# Space Complexity : O(1)


# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]