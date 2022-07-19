# Method-1

def waysToMakeFair(nums):
    even = 0
    odd = 0
    result = 0
    
    for i in range(1, len(nums)):
        if i % 2 == 0:
            even += nums[i]
        else:
            odd += nums[i]
    
    if even == odd:
        result += 1
        
    for i in range(1, len(nums)):
        if i % 2 == 0:
            even -= nums[i]
            even += nums[i-1]
        else:
            odd -= nums[i]
            odd += nums[i-1]

        if even == odd:
            result += 1
    
    return result

# Time Complexity : O(n)
# Space Complexity : O(1)