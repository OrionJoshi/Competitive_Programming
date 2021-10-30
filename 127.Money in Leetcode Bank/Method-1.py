# Method-1 Math

def totalMoney(n):
    totalMoney = 0
    counter = 0
    monday = 0
    
    for i in range(0, n):
        if i % 7 == 0:
            monday += 1
            totalMoney += monday
            counter = 0
            continue
        counter += 1
        totalMoney += (monday + counter)
        
    return totalMoney

# Time Complexity : O(n)
# Space Compexity : O(1)