# Method-1

def findDuplicates(nums):
    output = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            output.append(index + 1)
        
        nums[index] = - nums[index]
            
    return output

# Time Complexity : O(n)
# Space Complexity : O(1)

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]