# Method-2 Binary Search

def isPerfectSquare(num):
    if num == 1:
        return True
    left = 1
    right = num
    
    while left <= right:
        mid = (left + right ) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Time Complexity : O(logn)
# Space Complexity : O(1)