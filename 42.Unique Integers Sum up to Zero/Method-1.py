# Method-1 Iterative

def sumUpToZero(n):
    result = []
    if n == 1:
        return [0]
    else:
        if n % 2 != 0:
            result.append(0) 
        n = int(n/2)
        for i in range(1,n + 1):
            result.append(i)
            result.append(-i)
    return result

# Time Complexity : O(n)
# Space Complexity : O(n)