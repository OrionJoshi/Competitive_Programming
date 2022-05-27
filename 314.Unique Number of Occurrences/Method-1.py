# Method-1

def uniqueOccurrences(arr):
    dic = {}
    
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    if len(set(dic.values())) != len(set(arr)):
        return False
    
    return True

# Time Complexity : O(n)
# Space Complexity : O(n)