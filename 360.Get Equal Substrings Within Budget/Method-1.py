# Method-1

def equalSubstring(s, t, maxCost):
    l = 0
    cost = 0
    res = 0

    for r in range(len(s)):
        cost += abs(ord(s[r]) - ord(t[r]))
        while cost > maxCost:
            cost -= abs(ord(s[l]) - ord(t[l]))
            l+=1
        res = max(res,  r - l + 1)

    return res

# Time Complexity : O(n*n)
# Space Complexity : O(1)