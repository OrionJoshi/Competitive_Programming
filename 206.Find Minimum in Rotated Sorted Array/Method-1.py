# Method-1 Binary Search

def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        currElement = nums[mid]


        if currElement <= nums[right]:
            right = mid
        else:
            left = mid + 1
            
    return nums[left]

# Time Complexity : O(logn)
# Space Complexity : O(1)