# Method-1

def getLucky(s, k):
    t = ""
    for  i in s:
        t += str(ord(i) - ord('a') + 1)
    sm = 0
    while k > 0 :
        sm = 0
        for i in t:
            sm += int(i)
        t = str(sm)
        k -= 1
    return t

# Time Complexity : O(nk)
# Space Complexity : O(1)