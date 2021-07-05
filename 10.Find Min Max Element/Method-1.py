# # Method-1 Iterative method
def findMinMax(arr):
    arrayLength = len(arr)
    minElement = arr[0]
    maxElement = arr[0]
    for i in range(1, arrayLength):
        if minElement > arr[i]:
            minElement = arr[i]
        elif maxElement < arr[i]:
            maxElement = arr[i]
            
    return [minElement, maxElement]

# Time complexity : O(n)
# Space complexity : O(1)