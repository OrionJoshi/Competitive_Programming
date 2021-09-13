# Method-2 Using Pointers

def backspaceCompare(s, t):
    
    str1 = backspaceremove(s)
    str2 = backspaceremove(t)
    
    return True if str1 == str2 else False

def backspaceremove(s):
    count = 0
    lst = []

    for x in reversed(s):
        if x == '#':
            count += 1
        elif count != 0:
            count -= 1
        else:
            lst.append(x)
            
    return lst

# Time Complexity : O(max(n, m))
# Space Complexity : O(n + m)