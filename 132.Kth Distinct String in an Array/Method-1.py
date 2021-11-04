# Method-1 Hash table

def kthDistinct(arr, k):
    length = len(arr)
    mapping = {}
    
    for i in range(length):
        if arr[i] in mapping:
            mapping[arr[i]] += 1
        else:
            mapping[arr[i]] = 1
            
    for x in mapping:
        if mapping[x] == 1:
            k -= 1
        if k ==0:
            return x
    return ''

# Time Complexity : O(n)
# Space Complexity : O(n)