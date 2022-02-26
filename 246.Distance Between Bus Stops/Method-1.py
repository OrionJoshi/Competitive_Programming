# Method-1

def distanceBetweenBusStops(distance, start, destination):
    a = min(start,destination)
    b = max(start,destination)

    return min(sum(distance[a:b]),sum(distance) - sum(distance[a:b]))

# Time Complexity : O(n)
# Space Complexity : O(n)