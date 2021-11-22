# Method-1 Sorting

def classPhotos(redShirtHeights, blueShirtHeights):
    length = len(redShirtHeights)
    sorted(redShirtHeights)
    sorted(blueShirtHeights)
    
    redMax = redShirtHeights[-1]
    blueMax = blueShirtHeights[-1]
    
    redFirst = 1 if blueMax > redMax else 0
    
    for i in range(length):
        if redFirst and redShirtHeights[i] >= blueShirtHeights[i]:
            return False
        elif redFirst == 0 and blueShirtHeights[i] >= redShirtHeights[i]:
            return False
            
    return True

# Time Complexity : O(nlogn)
# Space Complexity : O(1)