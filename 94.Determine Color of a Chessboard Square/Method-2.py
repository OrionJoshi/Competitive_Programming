# Method-2

def squareIsWhite(coordinates):
    
    if ord(coordinates[0]) % 2 != 0 and int(coordinates[1]) % 2 != 0 \
    or ord(coordinates[0]) % 2 == 0 and int(coordinates[1]) % 2 == 0:
        return False
    else:
        return True

# Time Complexity : O(1)
# Space Complexity : O(1)
    