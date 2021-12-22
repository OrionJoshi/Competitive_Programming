# Method-1 Sorting

def findContentChildren(g, s):
    g.sort()
    s.sort()
    count = 0
    i = 0
    j = 0
    
    while i< len(g) and j < len(s):
        if s[j] >= g[i]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
            
    return count

# Time Complexity : O(nlogn)
# Space Complexity : O(1)