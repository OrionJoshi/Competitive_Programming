# Method-1

def triangleNumber(nums):
    length = len(nums)
    count = 0
    nums.sort()
    
    for i in range(2, length):
        left,right = 0, i - 1
        
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                count += (right - left)
                right -= 1
            else:
                left += 1
                
    return count

# Time Complexity : O(n^2)
# Space Complexity : O(1)