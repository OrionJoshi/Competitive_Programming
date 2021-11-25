# Method-1

def findBuildings(heights):
    result = []
    prevMaxHeight = None

    for i in range(len(heights) - 1, -1 , -1):
        height = heights[i]

        if not prevMaxHeight:
            result.append(i)
            prevMaxHeight = height
        else:
            if height > prevMaxHeight:
                result.append(i)
                prevMaxHeight = height

    return sorted(result)

# Time Complexity : O(nlogn)
# Space Complexity : O(n)