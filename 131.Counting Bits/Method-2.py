# Method-2 Using Count

def countBits(n):
    result = []
    for i in range(n + 1):
        binaryNum = "{0:b}".format(int(i))
        result.append(binaryNum.count('1'))
        
    return result

# Time Complexity : O(nlogn)
# Space Complexity : O(n)
    