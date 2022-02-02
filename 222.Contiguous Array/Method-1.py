# Method-1 Using Hash Table

def findMaxLength(nums):
    count = 0
    mapping = {0: -1}
    max_len = 0
    
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
        
        if count in mapping:
            max_len = max(max_len, i - mapping[count])
        else:
            mapping[count] = i
        
    return max_len

# Time Complexity : O(n)
# Space Complexity : O(n)