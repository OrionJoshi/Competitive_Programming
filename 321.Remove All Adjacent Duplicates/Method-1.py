# Method-1

def removeDuplicates(s, k):
    stack = [[s[0], 1]]

    for i in range(1, len(s)):
        if stack and s[i] == stack[-1][0]:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([s[i], 1])
    
    res = ""

    for ch, cnt in stack:
        res += ch * cnt
    
    return res

# Time Complexity : O(n)
# Space Complexity : O(n)