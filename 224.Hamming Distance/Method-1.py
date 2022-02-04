# Method-1 Using Bitwise

def hammingDistance(x, y):
    count = 0
    x = x ^ y
    
    while x:
        count += 1
        x = x & (x - 1)
        
    return count

# Time Complexity : O(1)
# Space Complexity : O(1)