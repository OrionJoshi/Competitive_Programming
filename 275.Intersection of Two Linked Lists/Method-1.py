# Method-1

def getIntersectionNode(headA, headB):
    h1 = headA
    h2 = headB
    while h1 != h2:
        h1 = h1.next if h1 else headB
        h2 = h2.next if h2 else headA
    return h1

# Time Complexity : O(n)
# Space Complexity : O(1)