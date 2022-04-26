# Method-1

def removeDuplicateLetters(s):
    result = ''

    while s:
        i = min(map(s.rindex, set(s)))
        c = min(s[:i+1])
        result += c
        s = s[s.index(c):].replace(c, '')

    return result

# Time Complexity : O(n)
# Space Complexity : O(n)