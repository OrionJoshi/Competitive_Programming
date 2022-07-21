# Method-1

def numberOfWays(s):
    Numzero = s.count('0')
    ones = len(s) - Numzero
    zeroPrefix = onePrefix = res = 0
    
    for char in s:
        if char == '0':
            res += onePrefix * (ones - onePrefix)
            zeroPrefix += 1
        else:
            res += zeroPrefix * (Numzero - zeroPrefix)
            onePrefix += 1
    
    return res

# Time Complexity : O(n)
# Space Complexity : O(1)