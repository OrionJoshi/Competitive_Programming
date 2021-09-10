# Method-2 Using Pointers

def moveZeroes(nums):
    zeroPtr = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zeroPtr] = nums[zeroPtr],  nums[i]
            zeroPtr += 1
    return nums

# Time Complexity :  O(n)
# Space Complexity : O(1)

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]