# Method-2 Sorting method

def findMinMax(arr):
    arrayLength = len(arr)
    
    # assuminig the use of best sorting algorithm
    arr.sort()
    minElement = arr[0]
    maxElement = arr[arrayLength - 1]
    return [minElement, maxElement]
    
# Time Complexity : O(nlogn)
# Space Complexity : O(1)