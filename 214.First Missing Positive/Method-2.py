# Method-2 Using Sorting

def firstMissingPositive(nums):
    nums.sort()
    
    currPositive = 1
    
    for num in nums:
        if num > 0:
            if num == currPositive:
                currPositive += 1
            else:
                if num < currPositive:
                    continue
                else:
                    return currPositive
                    
    return currPositive

# Time Complexity : O(nlogn)
# Space Complexity : O(1)