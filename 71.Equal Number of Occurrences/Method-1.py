# Method-1 

def areOccurencesEqual(s):
    length = len(s)
    mapping = {}
        
    for char in s:
        if char not in mapping:
            mapping[char] = 1
        else:
            mapping[char] += 1
            
    return True if len(list(set(list(mapping.values())))) == 1 else False

# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

# Time Complexity : O(n)
# Space Complexity : O(n)