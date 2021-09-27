# Method-1

def squareIsWhite(coordinates):
    mapping = {}
    
    for i in range(ord('a'), ord('h') + 1):
        mapping[chr(i)] = i
        
    firstChar = coordinates[0]
    secondChar = coordinates[1]
    
    if mapping[firstChar] % 2 != 0:
        if int(secondChar) % 2 != 0:
            return False
        else:
            return True
    else:
        if int(secondChar) % 2 != 0:
            return True
        else:
            return False

# Time Complexity : O(1)
# Space Complexity : O(1)

# Input: coordinates = "a1"
# Output: false
# Explanation: From the chessboard above,
#  the square with coordinates "a1" is black, so return false.