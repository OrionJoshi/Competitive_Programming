# Method-1 Using Math

def isBoomerang(points):
    dy1 = points[1][1] - points[0][1]
    dx1 = points[1][0] - points[0][0]
    
    dy2 = points[2][1] - points[1][1]
    dx2 = points[2][0] - points[1][0]
    
    if not ((dy2/dx2) == (dy1/dx1)):
        return True
    else:
        return False

# Time Complexity : O(1)
# Space Complexity : O(1)