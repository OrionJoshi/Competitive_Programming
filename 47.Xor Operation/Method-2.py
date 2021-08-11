# Method-1

def xorOperation(n, start):
    lst = []
    result = 0
    for i in range(n):
        lst.append(start + 2 * i)
    
    for i in range(n):
        result ^= lst[i]
        
    return result
    
# Time Complexity : O(n)
# Space Complexity : O(n)