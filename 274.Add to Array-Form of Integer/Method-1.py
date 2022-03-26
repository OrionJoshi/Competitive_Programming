# Method-1

def addToArrayForm(num, k):
    res  = []
    
    for i in reversed(range(len(num))):
        res.append((num[i] + k) % 10)
        k = (num[i] + k) // 10
        
    while k > 0:
        res.append(k % 10)
        k = k // 10
        
    return reversed(res)

# Time Complexity : O(n)
# Space Complexity : O(n)