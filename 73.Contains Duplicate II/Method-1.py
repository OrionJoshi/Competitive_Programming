# Method-1 Iterative Method

def containsNearbyDuplicate(nums, k):
    length = len(nums)
    
    for i in range(length):
        for j in range(length):
            if i == j:
                continue
            if nums[i] == nums[j]:
                if abs(i - j) <= k:
                    return True
                    
    return False

# Time Complexity : O(n^2)
# Space Complexity : O(1)