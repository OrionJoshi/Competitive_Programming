# Method-1 

def tribonacci(n):
    if n == 0:
        return n
    elif n == 1 or n == 2:
        return 1
    else:
        f1 = 0
        f2 = 1
        f3 = 1
        
        for i in range(3, n + 1):
            temp = f1 + f2 + f3
            f1 = f2
            f2 = f3
            f3 = temp
            
    return f3

# Time Complexity : O(n)
# Space Complexity : O(1)