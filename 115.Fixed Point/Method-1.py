# Method-1 Binary Search

def fixedPoint(arr):
    first = 0
    last = len(arr) - 1
    
    
    while first < last:
        mid = (first + last) // 2
        
        if mid == arr[mid]:
            return mid
        if mid < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return -1

# Time Complexity : O(logn)
# Space Complexity : O(1)
