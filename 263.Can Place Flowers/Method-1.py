# Method-1

def canPlaceFlowers(flowerbed, n):
    count, prev = 0, 0

    for cur in flowerbed:
        if cur == 1:
            if prev == 1:
                count -= 1
            prev = 1
        else:
            if prev == 1:
                prev = 0 
            else:
                count += 1
                prev = 1 
        
    return count >= n

# Time Complexity : O(n)
# Space Complexity : O(1)