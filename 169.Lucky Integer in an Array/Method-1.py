# Method-1

def findLucky(arr):
    mapping = {}
    largest = -1
    
    for i in range(len(arr)):
        if arr[i] not in mapping:
            mapping[arr[i]] = 1
        else:
            mapping[arr[i]] += 1
    
    for i,value in enumerate(mapping):
        currValue = mapping[value] 
        if value == currValue and largest < currValue:
            largest = currValue
            
    return largest
    
# Time Complexity : O(n)
# Space Complexity : O(n)