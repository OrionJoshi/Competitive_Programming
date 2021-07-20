# Method-2 Iterative Method

def concatArray(lst):
    resultList = []
    lengthOfList = len(lst)
    
    for i in range(0, 2 * lengthOfList):
        if i >= lengthOfList:
            resultList.append(lst[i - lengthOfList])
        else:
            resultList.append(lst[i])
    return resultList

# Time Complexity : O(n)
# Space Complexity : O(n)