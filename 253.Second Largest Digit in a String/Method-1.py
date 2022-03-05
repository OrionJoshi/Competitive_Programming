# Method-1

def secondHighest(s):
    l = []

    for i in s:
        if i.isdigit() and i not in l:
            l.append(i)
    if len(l) >= 2:
        return int(sorted(l)[-2])
    else:
        return -1

# Time Complexity : O(n)
# Space Complexity : O(n)