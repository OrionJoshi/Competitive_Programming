# Method-1

def fairCandySwap(aliceSizes, bobSizes):
    
    diff = (sum(aliceSizes)-sum(bobSizes))//2
    setA = set(aliceSizes)
    for b in set(bobSizes):
        if diff+b in setA:
            return [diff+b, b]
    return []

# Time Complexity : O(n * m)
# Space Complexity : O(1)

# Input: aliceSizes = [1,1], bobSizes = [2,2]
# Output: [1,2]