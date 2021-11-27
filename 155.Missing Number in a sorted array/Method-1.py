# Method-1 Binary Search

def missingNum(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if mid + 1 != nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left + 1

# Time Complexity : O(logn)
# Space Complexity : O(1)