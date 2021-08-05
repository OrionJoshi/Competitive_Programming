# Method-1
def evenNoOfDigits(lst):
    length = len(lst)
    totalNum = 0
    
    for x in lst:
        count = 0
        while x != 0:
            x = int(x / 10)
            count += 1
        if count % 2 == 0:
            totalNum += 1
        
    return totalNum
    
print(evenNoOfDigits([555,901,482,1771]))

# Time Complexity : O(n*m)
# Space Complexity : O(1)