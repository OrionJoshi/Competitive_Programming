# Method-1 Binary Search

def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (right + left) // 2
        currElement = nums[mid]
        if currElement == target:
            return mid
        
        if nums[left] <= currElement:
            if target > currElement or nums[left] > target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target > nums[right] or target < currElement:
                right = mid -1
            else:
                left = mid + 1
    return -1

# Time Complexity : O(logn)
# Space Complexity : O(1)