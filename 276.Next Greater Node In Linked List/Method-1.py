# Method-1

def nextLargerNodes(head):
    pos = -1
    stack = []
    ans = []
    
    while head:
        pos += 1
        ans.append(0)
        while stack and stack[-1][1] < head.val:
            idx, _ = stack.pop()
            ans[idx] = head.val

        stack.append((pos, head.val))
        head = head.next
    return ans

# Time Complexity : O(n^2)
# Space Complexity : O(n)