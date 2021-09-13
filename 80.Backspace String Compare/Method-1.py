# Method-1 Using Stack

def backspaceCompare(s, t):
    list1 = []
    list2 = []
    
    for x in s:
        if x == '#':
            if len(list1) != 0:
                list1.pop()
        else:
            list1.append(x)
            
    for y in t:
        if y == '#':
            if len(list2) != 0:
                list2.pop()
        else:
            list2.append(y)
    
    return True if list1 == list2 else False

# Time Complexity : O(max(n, m))
# Space Complexity : O(n + m)