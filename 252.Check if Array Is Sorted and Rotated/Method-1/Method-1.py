# Method-1

def check(nums):
    flag = False

    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            if flag:
                return False
            flag = True
        
        if flag and nums[i] > nums[0]:
            return False

    return True

# Time Complexity : O(n)
# Space Complexity : O(1)