# Method-1

def isMonotonic(nums):
    isMonotoneInc = True
    isMonotoneDec = True
    i = 0
    length = len(nums)

    while i < length - 1 and isMonotoneInc:
        if nums[i] > nums[i + 1]:
            isMonotoneInc = False
        i += 1

    if isMonotoneInc:
        return True
    else:
        i = 0
        while i < length - 1 and isMonotoneDec:
            if nums[i] < nums[i + 1]:
                isMonotoneDec = False
            i += 1

    return isMonotoneDec

# Time Complexity : O(n)
# Space Complexity : O(1)

# Input: nums = [1,2,2,3]
# Output: true