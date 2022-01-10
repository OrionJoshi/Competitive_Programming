# Method-1 Sorting

def reductionOperations(nums):
    nums.sort()
    curr = result = 0
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            curr += 1
        result += curr
    return result

# Time Complexity : O(n)
# Space Complexity : O(1)