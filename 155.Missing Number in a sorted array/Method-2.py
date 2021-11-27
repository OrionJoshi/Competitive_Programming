# Method-2 Iterative

def missingNum(nums):
    length = len(nums)
    
    for i in range(length):
        if i + 1 != nums[i]:
            break
    return i + 1
    

# Time Complexity : O(n)
# Space Complexity : O(1)