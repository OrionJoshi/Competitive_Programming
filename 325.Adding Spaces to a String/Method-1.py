# Method-1

def addSpaces(s, spaces):
    arr=[]
    prev=0
    
    for i in spaces:
        arr.append(s[prev:i])
        prev=i
    arr.append(s[i:])
    
    return " ".join(arr)

# Time Complexity : O(n)
# Space Complexity : O(n)