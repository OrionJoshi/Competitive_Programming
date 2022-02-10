# Method-1

def minimumCost(cost):
    cost.sort(reverse = True)
    totalCost = 0

    itemIdx = 0

    while itemIdx < len(cost):
        totalCost += sum(cost[itemIdx: itemIdx + 2])
        itemIdx += 3

    return totalCost

# Time Complexity : O(nlogn)
# Space Complexity : O(1)