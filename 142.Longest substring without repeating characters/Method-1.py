# Method-1

def areDistinct(strr, i, j):
    # Note : Default values in visited are false
    visited = [0] * (26)
 
    for k in range(i, j + 1):
        if (visited[ord(strr[k]) - ord('a')] == True):
          return False
             
        visited[ord(strr[k]) - ord('a')] = True
 
    return True
 
# Returns length of the longest substring
# with all distinct characters.
def longestUniqueSubsttr(strr):   
    n = len(strr)
    res = 0
     
    for i in range(n):
        for j in range(i, n):
            if (areDistinct(strr, i, j)):
                res = max(res, j - i + 1)
                 
    return res

# Time Complexity : O(n3)
# Space Complexity : O(1)