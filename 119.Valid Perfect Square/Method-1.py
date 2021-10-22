# Method-1 Math

def isPerfectSquare(num):
    x = num ** 0.5 - int(num ** 0.5)
    
    if (x):
        return False
    else:
        return True

# Time Complexity : O(1)
# Space Complexity : O(1)