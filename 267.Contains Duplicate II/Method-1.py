# Method-1

def containsNearbyDuplicate(nums, k):
    if len(set(nums)) == len(nums):
        return False  
    
    for i in range(len(nums)):
        if len(nums[i : i + k + 1]) != len(set(nums[i : i + k + 1])):
            return True
        
    return False

# Time Complexity : O(n)
# Space Complexity : O(1)