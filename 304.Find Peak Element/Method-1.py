# Method-1

def findPeakElement(nums):
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1

        return left

# Time Complexity : O(logn)
# Space Complexity : O(1)