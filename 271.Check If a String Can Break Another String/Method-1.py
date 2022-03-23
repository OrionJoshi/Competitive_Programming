# Method-1

from collections import Counter

def checkIfCanBreak(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    diff = 0
    s = set()

    for i in range(26):
        c = chr(ord('a') + i)
        diff += c1[c] - c2[c]

        if diff:
            s.add(diff > 0)

    return len(s) < 2

# Time Complexity : O(n)
# Space Complexity : O(n)