# Method-1

def firstUniqChar(s):
    counter = {}
    
    for i, ch in enumerate(s):
        if ch in counter:
            counter[ch] = -1
        else:
            counter[ch] = i
            
    for ch in s:
        if counter[ch] !=-1:
            return counter[ch]
        
    return -1

# Time Complexity : O(n)
# Space Complexity : O(n)