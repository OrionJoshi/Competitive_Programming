# Method-1

def largestAltitude(gain):
    maxAltitude = 0
    currentAltitude = 0
    
    for alt in gain:
        currentAltitude = currentAltitude + alt
        if currentAltitude > maxAltitude:
            maxAltitude = currentAltitude
            
    return maxAltitude

# Time Complexity : O(n)
# Space Complexity : O(1)