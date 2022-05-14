#Method-1

def hIndex(citations):
    n , left , right = len(citations) , 0 , len(citations)

    while left < right:
        mid = left + (right - left) // 2
        numGreater = n - mid
        if numGreater <= citations[mid]:
            right = mid
        else:
            left = mid + 1

    return n - left

# Time Complexity : O(logn)
# Space Complexity : O(1)