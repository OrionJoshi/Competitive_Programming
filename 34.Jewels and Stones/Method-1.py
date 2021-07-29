# Method-1 Iterative
def jewelsAndStones(jewels, stones):
    count = 0
    for jewel in jewels:
        for stone in stones:
            if jewel == stone:
                count += 1
                
    return count

# Time Complexity : O(n * m)
# Space Complexity : O(1)