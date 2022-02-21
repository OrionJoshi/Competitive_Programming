# Method-1

def decrypt(code, k):
    length = len(code)
    result = []
    
    if k == 0:
        return [0 for _ in code]
    elif k > 0:
        for i in range(length):
            if i + k > length - 1:
                remPos = k - (length - i - 1)
                result.append(sum(code[i + 1:]) + sum(code[0: remPos]))
            else:
                result.append(sum(code[i+1: i + k + 1]))
    else:
        for i in range(length):
            rem = abs(k) - i 
            if rem < 0:
                result.append(sum(code[i - abs(k): i]))
            else:
                result.append(sum(code[0: i]) + sum(code[::-1][0: rem]))
            
    return result

# Time Complexity : O(n)
# Space Complexity : O(n)