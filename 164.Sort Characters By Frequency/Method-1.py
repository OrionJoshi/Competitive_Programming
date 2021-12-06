# Method-1

def frequencySort(s):
    mapping = {}
    result = []
    for i in range(len(s)):
        if s[i] not in mapping:
            mapping[s[i]] = 1
        else:
            mapping[s[i]] += 1
    
    sortList = sorted(mapping.items(), key=lambda x: x[1], reverse=True)
    
    for i in range(len(sortList)):
        result = result + (list(sortList[i][0]) * sortList[i][1])
        
    return ''.join(result)

# Time Complexity : O(nlogn)
# Space Complexity : O(n + m)