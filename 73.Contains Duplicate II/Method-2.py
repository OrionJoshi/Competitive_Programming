# Method-2 Using Hash
def containsNearbyDuplicate(nums, k):
    length = len(nums)
    mapping = {}
    
    for i in range(length):
        if nums[i] not in mapping:
            mapping[nums[i]] = i
        else:
            if abs(i - mapping[nums[i]]) <= k:
                return True
            else:
                mapping[nums[i]] = i
    return False

# Time Complexity : O(n)
# Space Complexity : O(n)