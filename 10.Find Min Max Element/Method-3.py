# Method-3 Recursive Method

def findMinMax(arr, left, right):
    if left == right:
        return [arr[left], arr[right]]
    elif (right - left == 1):
        return [arr[left], arr[right]] if arr[left] < arr[right] else [arr[right], arr[left]]
    else:
        mid = int((left + right)/2)
        [minElement, maxElement] = findMinMax(arr, left, mid)
        [minElement2, maxElement2] = findMinMax(arr, mid + 1, right)
        
        if minElement > minElement2:
            minElement = minElement2
        if maxElement < maxElement2:
            maxElement = maxElement2
            
    return [minElement, maxElement]
    
# Time Complexity : O(n)
# Space Complexity : O(1)