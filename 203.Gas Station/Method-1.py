# Method-1 Using Greedy

def canCompleteCircuit(gas, cost):
    totalGas = 0
    total = 0
    idx = 0
    
    for i in range(len(gas)):
        currGas = gas[i] - cost[i]
        totalGas += currGas
        
        if totalGas < 0:
            idx = i + 1
            totalGas = 0
        total += currGas
    return idx if total >= 0 else -1 

# Time Complexity : O(n)
# Space Complexity : O(1)