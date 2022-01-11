# Method-2

def maxDistance(colors):
    maxDistance = 0

    for i in range(len(colors)):
        for j in range(len(colors)):
            if colors[i] != colors[j]:
                currentDis = abs(i - j)
                if currentDis > maxDistance:
                    maxDistance = currentDis
    return maxDistance

# Time Complexity : O(n^2)
# Space Complexity : O(1)