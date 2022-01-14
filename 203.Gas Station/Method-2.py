# Method-2 Using Brute Force

def canCompleteCircuit(gas, cost):
    length = len(gas)
    for i in range(len(gas)):
        totalCost = 0
        totalStep = 0
        j = i
        
        while totalStep < length:
            currIdx = j % length
            totalCost += gas[currIdx] - cost[currIdx]
            
            if totalCost < 0:
                break
            j += 1
            totalStep += 1
        
        if totalStep == length and totalCost >= 0:
            return i
    return -1

# Time Complexity : O(n^2)
# Space Complexity : O(1)