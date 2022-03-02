# Method-1

def addToArrayForm(A, K):
    num = ''

    for elem in A:
        num = num + str(elem)
    sum = int(num) + K
    
    A = [int(d) for d in str(sum)]

    return A

# Time Complexity : O(n)
# Space Complexity : O(n)