# Method-1

def pancakeSort(arr):
    res = []
    for x in range(len(arr), 1, -1):
        i = arr.index(x)
        res.extend([i + 1, x])
        arr = arr[:i:-1] + arr[:i]
    return res

# Time Complexity : O(n)
# Space Complexity : O(n)