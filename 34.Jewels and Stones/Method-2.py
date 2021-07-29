# Method-2 Using Hashing
def jewelsAndStones(jewels, stones):
    count = 0
    mapping = {}
    
    for jewel in jewels:
        mapping[jewel] = 1
        
    for stone in stones:
        if stone in mapping:
            count += 1
            
    return count

# Time Complexity : O(n)
# Space Complexity : O(m)
# where n = no of stones
#       m = no of jewels