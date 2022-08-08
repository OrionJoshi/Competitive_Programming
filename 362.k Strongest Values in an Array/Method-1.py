# Method-1

def getStrongest(arr, k):
    arr.sort()
    median = arr[(len(arr) - 1) // 2]
    res = []
    left, right = 0, len(arr) - 1

    for _ in range(k):
        if median - arr[left] > arr[right] - median:
            res.append(arr[left])
            left += 1
        else:
            res.append(arr[right])
            right -= 1
    
    return res

# Time Complexity : O(nlogn)
# Space Complexity : O(n)