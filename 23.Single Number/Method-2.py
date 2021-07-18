# Method-2 using List operation

def singleNumber(lst):
    finalNum = []
    for x in lst:
        if x in finalNum:
            finalNum.remove(x)
        else:
            finalNum.append(x)
            
    return finalNum[0]
    
# Time Complexity : O(n^2)
# Space Complexity : O(n)