# Method-1

def customSortString(order, s):
    lst = list(s)
    res = ""
    for i in order:
        while i in lst:
            res += i
            lst.remove(i)
    res += ''.join(lst)
    return (res)

# Time Complexity : O(n)
# Space Complexity : O(n)