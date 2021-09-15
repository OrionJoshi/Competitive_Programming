# Method-1 Using Pointers

def sortArrayByParityII(nums):
    evenPtr = 0
    oddPtr = 1
    
    while evenPtr < len(nums) and oddPtr < len(nums):
        if nums[evenPtr] % 2 == 0:
            evenPtr += 2
        else:
            if nums[oddPtr] % 2 != 0:
                oddPtr += 2
            else:
                nums[evenPtr], nums[oddPtr] = nums[oddPtr], nums[evenPtr]
                evenPtr += 2
                oddPtr += 2
            
    return nums

# Time Complexity : O(n)
# Space Complexity : O(1)

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
