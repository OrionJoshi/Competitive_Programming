# Method-1 Using Dictionary

def uniqueOccurrences(arr):
    mapping = {}
    
    for i in arr:
        if i in mapping:
            mapping[i] += 1
        else:
            mapping[i] = 1
    
    if len(set(mapping.values())) != len(set(arr)):
        return False
    return True

# Time Complexity : O(n)
# Space Complexity : O(n)

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. 
# No two values have the same number of occurrences.