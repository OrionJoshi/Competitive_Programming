# Method-1

import math

def smallestDivisor(nums, threshold):
    l, r = 1, max(nums)
    
    while l <= r:
        mid = (l + r) // 2
        if sum(math.ceil(num / mid) for num in nums) > threshold:
            l = mid + 1
        else:
            r = mid - 1
    return l

# Time Complexity : O(nlogn)
# Space Complexity : O(1)