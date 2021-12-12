# Method-1

def thirdMax(nums):
    nums.sort(reverse = True)
    largest = nums[0]
    count = 1
    
    for i in range(1, len(nums)):
        if largest > nums[i]:
            largest = nums[i]
            count += 1
        if count == 3:
            return largest
    return nums[0]

# Time Complexity : O(nlogn)
# Space Complexity : O(1)