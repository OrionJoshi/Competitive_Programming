# Method-1

import math
from bisect import bisect_left

def findRadius(houses, heaters):
    nHeater = len(heaters)
    heaters.sort()
    maxDistance = - math.inf
    for house in houses:
        index = bisect_left(heaters, house)
        if index == 0:
            maxDistance = max(maxDistance, abs(house-heaters[index]))
        elif index == nHeater:
            maxDistance = max(maxDistance, abs(house-heaters[index-1]))
        else:
            maxDistance = max(maxDistance, min(abs(house-heaters[index-1]), abs(house-heaters[index])))
    return maxDistance

# Time Complexity : O(nlogn)
# Space Complexity : O(1)