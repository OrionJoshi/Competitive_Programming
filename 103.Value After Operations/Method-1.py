# Method-1

def finalValueAfterOperations(operations):
    total = 0
    
    for op in operations:
        if op[1] == '-':
            total -= 1
        else:
            total += 1
            
    return total

# Time Complexity : O(n)
# Space Complexity : O(1)


# Input: operations = ["--X","X++","X++"]
# Output: 1
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# --X: X is decremented by 1, X =  0 - 1 = -1.
# X++: X is incremented by 1, X = -1 + 1 =  0.
# X++: X is incremented by 1, X =  0 + 1 =  1.