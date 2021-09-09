# Method-1 Using Set

def checkIfExist(lst):
    available  = set()
    
    for num in lst:
        if num / 2 in available  or num * 2 in available :
            return True
        available .add(num)
    return False

# Time Complexity : O(n)
# Space Complexity : O(n)

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.