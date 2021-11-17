# Method-1 Simulation

def getMaximumGenerated(n):
    if n == 0 or n == 1:
        return n

    result = [None] * (n + 1)
    result[0] = 0
    result[1] = 1

    for i in range(2, n + 1):
        if i % 2 == 0:
            result[i] = result[int(i / 2)]
        else:
            div = int(i // 2)
            result[i] = result[div] + result[div + 1]
            
    return max(result)
    
# Time Complexity : O(n)
# Space Complexity : O(n)