# Method-1 Using Stack

def removeDuplicates(self, s: str) -> str:
    stack = []

    for x in s:
        if stack:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
        else:
            stack.append(x)
    return ''.join(stack)

# Time Complexity : O(n)
# Space Complexity : O(n)