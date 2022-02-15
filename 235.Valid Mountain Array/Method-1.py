# Method-1

def validMountainArray(arr):
    length = len(arr)
    i = 0

    while i + 1 < length and arr[i] < arr[i + 1]:
        i += 1
    
    if i == 0 or i == length - 1:
        return False
        
    while i + 1 < length and arr[i] > arr[i + 1]:
        i += 1
        
    return i == length - 1

# Time Complexity : O(n)
# Space Complexity : O(1)