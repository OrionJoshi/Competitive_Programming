# Method-1 Using DP

def maxProduct(nums):
    maxProduct = max(nums)
    currMax = nums[0]
    currMin = nums[0]
    
    for num in nums:
        if num == 0:
            currMax , currMin = 1, 1
            continue
        temp = currMax
        currMax = max(currMax * num, currMin * num, num)
        currMin = min(temp * num, currMin * num, num)
        maxProduct = max(maxProduct, currMax)
        
    return maxProduct

# Time Complexity : O(n)
# Space Complexity : O(1)