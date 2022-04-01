# Method-1

def buddyStrings(A, B):
    diff = []
    
    if len(A) != len(B): 
        return False
    if A == B:
        return True if len(A) - len(set(A)) >= 1 else False
    
    for i in range(len(A)):
        if A[i] != B[i]:
            diff.append(i)
            if len(diff) > 2: return False
            
    if len(diff) != 2: return False
    
    if A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
        return True
    
    return False

# Time Complexity : O(n)
# Space Complexity : O(n)