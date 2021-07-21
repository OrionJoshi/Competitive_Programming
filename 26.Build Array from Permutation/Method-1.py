# Method-1 Using Extra List

def buildArray(lst):
    resultList = []
    length = len(lst)
    
    for i in range(length):
        resultList.append(lst[lst[i]])
    return resultList

# Time Complexity : O(n)
# Space Complexity : O(n)
