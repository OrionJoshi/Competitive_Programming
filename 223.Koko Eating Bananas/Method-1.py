#Method-1 Binary Search

import math

def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)
            
        if hours <= h:
            result = min(result, mid)
            right = mid - 1
        else:
            left = mid + 1
            
    return result

# Time Complexity : O(log(piles) * n)
# Space Complexity : O(1)