# Method-1 Binary Search

def singleNonDuplicate(nums):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = left + (right - left) // 2
        if not (mid%2 == 0 and mid+1 < len(nums) and nums[mid] == nums[mid+1]) and not (mid%2 == 1 and nums[mid] == nums[mid-1]):
            right = mid-1
        else:
            left = mid+1
            
    return nums[left]

# Time Complexity : O(logn)
# Space Complexity : O(1)