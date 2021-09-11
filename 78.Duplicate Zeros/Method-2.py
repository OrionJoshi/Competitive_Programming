# Method-2 Using Pointers

def duplicateZeros(nums):
    noOfZeros = nums.count(0)
    length = len(nums)
    i = length - 1
    j = length + noOfZeros - 1
    
    while i != j:
        if j < length:
            nums[j] = nums[i]
        j -= 1
        if nums[i] == 0:
            if j < length:
                nums[j] = nums[i]
            j -= 1
        i -= 1
    return nums

# Time Complexity  : O(n)
# Space Complexity : O(1)

# Input: nums = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
    