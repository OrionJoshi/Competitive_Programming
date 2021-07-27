# Method-1: Using Modulo

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

# Time Complexity : O(n*m)
#   n = length of list
#   m = longest digits of elements of list
# Space Complexity : O(1)