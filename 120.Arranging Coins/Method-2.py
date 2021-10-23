# Method-2 Binary Search

def arrangeCoins(n):
    left = 0
    right = n
    
    while left <= right:
        mid = (left + right) // 2
        curr = mid * (mid + 1) / 2
        if curr == n:
            return mid
        elif curr < n:
            left = mid + 1
        else:
            right = mid - 1
            
    return right

# Time Complexity : O(logn)
# Space Complexity : O(1)