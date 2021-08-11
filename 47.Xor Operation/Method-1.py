# Method-1

def xorOperation(n, start):
    result = 0
    
    for i in range(n):
        result ^= start + 2 * i
    return result

#  Time Complexity : O(n)
#  Space Complexity : O(1)
    