# Method-1

def minOperations(boxes):
    arr = []
    for i in range(len(boxes)):
        sumi = 0
        for j in range(len(boxes)):
            if(boxes[j] == '1'):
                sumi += abs(j - i)
        arr.append(sumi)
    
    return arr

# Time Complexity : O(n*n)
# Space Complexity : O(n)