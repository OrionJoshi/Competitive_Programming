# Method-1

def maxDistance(colors):
    length = len(colors)
    i, j = 0, length - 1
    
    while colors[0] == colors[j]:
        j -= 1
    while colors[-1] == colors[i]:
        i += 1
    return max(length - 1 - i , j)

# Time Complexity : O(n)
# Space Complexity : O(1)