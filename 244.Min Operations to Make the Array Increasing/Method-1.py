# Method-1

def minOperations(nums):
    ans = 0
    prev = -float('inf')
    
    for val in nums:
        if val > prev:
            prev = val
        else:
            ans += prev + 1 - val
            prev += 1
    return ans

# Time Complexity : O(n)
# Space Complexity : O(1)