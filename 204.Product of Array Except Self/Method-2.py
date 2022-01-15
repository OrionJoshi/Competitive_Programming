# Method-2

def productExceptSelf(nums):
    countZero = 0
    product = 1
    nonZeroProduct = 1
    
    for i in range(len(nums)):
        if nums[i] == 0:
            countZero += 1
        else:
            nonZeroProduct *= nums[i]
        
        product *= nums[i]
        
    for i in range(len(nums)):
        if nums[i] == 0 and countZero >= 2:
            nums[i] = 0
        elif nums[i] == 0:
            nums[i] = nonZeroProduct
        elif nums[i] != 0:
            nums[i] = int(product / nums[i])
    return nums

# Time Complexity : O(n)
# Space Complexity : O(1)