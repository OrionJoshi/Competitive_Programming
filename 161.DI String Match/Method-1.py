# Method-1 

def diStringMatch(S):
    result = []
    left = 0
    right = len(S)
    
    for x in S:

        if x == 'I':
            result.append(left)
            left += 1
        else:
            result.append(right)
            right -= 1

    result.append(right)

    return result

# Time Complexity : o(n)
# Space Complexity : O(n)