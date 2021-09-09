# Method-2 Iterative Method

def checkIfExist(lst):
    
    length = len(lst)
    
    for i in range(length):
        for j in range(length):
            if i == j:
                continue
            else:
                if lst[i] / 2 == lst[j] or lst[i] * 2 == lst[j]:
                    return True
    return False


# Time Complexity : O(n^2)
# Space Complexity : O(1)

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.