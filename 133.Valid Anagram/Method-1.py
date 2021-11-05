# Method-1 Hash table

def isAnagram(s, t):
    mapping = {}
    
    for x in s:
        if x  in mapping:
            mapping[x] += 1
        else:
            mapping[x] = 1
    for y in t:
        if y in mapping:
            mapping[y] -= 1
            
    return all(x == 0 for x in mapping.values()) and len(s) == len(t)

# Time Complexity : O(n)
# Space Complexity : O(n)