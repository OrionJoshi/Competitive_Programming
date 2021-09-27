# Method-3

def squareIsWhite(coordinates):
    
    coordinateSum = ord(coordinates[0]) + int(coordinates[1])
    
    if coordinateSum&1:
        return True
    else:
        return False

# Time Complexity : O(1)
# Space Complexity : O(1)