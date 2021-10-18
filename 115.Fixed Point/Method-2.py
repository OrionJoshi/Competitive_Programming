# Method-2 Iterative

def fixedPoint(arr):
    length = len(arr)
    
    for i in range(length):
        if i == arr[i]:
            return i
    return -1
    
# Time Complexity : O(n)
# Space Complexity : O(1)