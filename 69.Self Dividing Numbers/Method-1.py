# Method-1

def selfDividingNumbers(left, right):
    result = []
    
    for i in range(left, right + 1):
        count = 0
        
        for s in str(i):
            if s == '0' or i % int(s) != 0:
                break
            else:
                count += 1
                continue
        if count == len(str(i)):
            result.append(i)
            
    return result

# Time complexity : O(nlogm)
# Space Complexity : O(n)