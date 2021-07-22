# Method-2 Using Dynamic Programmming

def runningSum(lst):
    currentSum = lst[0]
    for i in range(1,len(lst)):
        currentSum += lst[i]
        lst[i] = currentSum
        
    return lst

# Time Complexity : O(n)
# Space Complexity : O(1)