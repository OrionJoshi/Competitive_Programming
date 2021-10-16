# Method-1 Iterative 

def peakIndexInMountainArray(arr):
    length = len(arr)
    
    for i in range(length):
        if arr[i] < arr[i + 1]:
            continue
        else:
            return i

# Time Complexity : O(n)
# Space Complexity : O(1)