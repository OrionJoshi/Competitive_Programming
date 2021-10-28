# Method-1 Using Binary Search

def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        currElem = nums[mid]
        if currElem == target:
            return mid
        elif currElem < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left if currElem > target else left

# Time Complexity : O(logn)
# Space Complexity : O(1)