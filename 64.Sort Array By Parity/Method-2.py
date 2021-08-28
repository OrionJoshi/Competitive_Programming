# Method-1 

def sortArrayByParity(nums):
    ptr = 0
    
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    
    return nums

# Time Complexity: O(n)
# Space Complexity: O(1)