# Method-1

def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if target in [nums[mid], nums[right], nums[left]]: 
            return True
        elif nums[mid]==nums[left] or nums[mid]==nums[right]:
            right -= 1
            left += 1
        elif nums[left] <= nums[mid]:
            if nums[left] < target < nums[mid]: right = mid - 1
            else: left = mid + 1
        else:
            if nums[mid] < target < nums[right]: 
                left = mid + 1
            else: 
                right = mid - 1
    return False

# Time Complexity : O(logn)
# Space Complexity : O(1)