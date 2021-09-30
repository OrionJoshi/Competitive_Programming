# Method-1 Using Sort

def missingNumber(nums):
    length = len(nums)
    nums.sort()
    
    for i in range(length):
        if i != nums[i]:
            return i
    return i + 1

# Time Complexity : O(nlogn)
# Space Complexity : O(n)

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers,
# so all numbers are in the range [0,3]. 2 is the missing number 
# in the range since it does not appear in nums.
