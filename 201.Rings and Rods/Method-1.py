# Method-1

def countPoints(rings):
    count = 0
    rods = [''] * 10
    
    for i in range(1, len(rings), 2):
        rods[int(rings[i])] += rings[i - 1]
        
    for rod in rods:
        if 'R' in rod and 'G' in rod and 'B' in rod:
            count += 1
    return count

# Time Complexity : O(n*m)
# Space Complexity : O(1)