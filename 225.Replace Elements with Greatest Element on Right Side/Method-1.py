# Method-1 

def replaceElements(arr):
    result = [-1]
    currGreatest = 0
    
    for num in arr[::-1]:
        if currGreatest < num:
            currGreatest = num
        result.append(currGreatest)
    result.pop()
    
    return result[::-1]

# Time Complexity : O(n)
# Space Complexity : O(n)