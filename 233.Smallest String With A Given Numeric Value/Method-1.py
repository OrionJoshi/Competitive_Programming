# Method-1

def getSmallestString(n, k):
    res = ['a'] * n
    val = n
    
    for i in range(n - 1, -1, -1):
        if val == k:
            break
        val -= 1
        res[i] = chr(96 + min(k - val, 26))
        val += ord(res[i]) - 96
        
    return ''.join(res)

# Time Complexity : O(n)
# Space Complexity : O(n)