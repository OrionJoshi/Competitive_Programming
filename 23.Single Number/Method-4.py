# Method-4 Using Math and Set
def singleNum(lst):
    singleElementsList = set(lst)
    return 2 * sum(singleElementsList) - sum(lst)
    
# Time Complexity : O(n)
# Space Complexity : O(n)