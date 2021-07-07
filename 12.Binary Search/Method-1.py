# Method-1 Iterative Method

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:

        mid = int((left + right) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1
    
# Time Complexity : O(logn)
# Space Complexity : O(1)