# Method-1  Using Binary Search

def mySqrt(num):
    left = 1
    right = num
    
    if num < 2:
        return num
    
    while left < right:
        mid = left + ((right - left)) // 2
        
        if mid * mid == num:
            return mid
        elif mid * mid > num:
            right = mid
        elif mid * mid < num:
            left = mid + 1
            
    return left - 1

# Time Complexity : O(logN)
# Space Complexity : O(1)