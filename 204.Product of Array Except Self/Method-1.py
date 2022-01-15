# Method-1

def productExceptSelf(nums):
    res = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) -1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

# Time Complexity : O(n)
# Space Complexity : O(1)