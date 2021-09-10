# Method-1

def moveZeroes(nums):
    zeroOccurence = nums.count(0)
    
    result = list(filter(lambda a: a!= 0, nums))
    
    for i in range(zeroOccurence):
        result.append(0)
        
    for i in range(len(result)):
        nums[i] = result[i]
        
    return nums

# Time Complexity :  O(n)
# Space Complexity : O(n)

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]