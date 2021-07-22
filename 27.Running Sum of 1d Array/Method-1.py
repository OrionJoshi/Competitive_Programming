# Method-1 Iterative Method

def runningSum(lst):
    for i in reversed(range(len(lst))):
        totalSum = 0
        for j in reversed(range(i + 1)):
            totalSum += lst[j]
        lst[i] = totalSum
    return lst
        
# Time Complexity : O(n^2)
# Space Complexity : O(1)