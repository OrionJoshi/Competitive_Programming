# Method-2 Binary Search

def peakIndexInMountainArray(arr):
    length = len(arr)
    first = 0
    last = length - 1
    
    while first < last:
        mid = int((first + last) / 2)
        
        if arr[mid] < arr[mid + 1]:
            first = mid + 1
        else:
            last = mid
    return first

# Time Complexity : O(logn)
# Space Complexity : O(1)