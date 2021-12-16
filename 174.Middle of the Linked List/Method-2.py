# Method-2

def middleNode(head):
    arr = [head]
    while arr[-1].next:
        arr.append(arr[-1].next)
        
    return arr[len(arr) // 2]

# Time Complexity : O(n)
# Space Complexity : O(n)
