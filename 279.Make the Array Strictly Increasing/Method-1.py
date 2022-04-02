# Method-1

import math

def canBeIncreasing(nums):
    prev = 0
    flag = False
    nums.append(math.inf)
    i, n = 0, len(nums) - 1
    while i < n:
        if prev < nums[i] < nums[i+1]:
            prev = nums[i]
        else:
            if flag:
                return False
            flag = True
            if nums[i+1] <= prev:
                prev = nums[i]
                i += 1
        i += 1
    
    return True

# Time Complexity : O(n)
# Space Complexity : O(1)