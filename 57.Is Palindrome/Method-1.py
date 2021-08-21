# Method-1 Using pointers

def isPalindrome(num):
    numString = str(num)
    leftPtr = 0
    rightPtr = len(numString) - 1
    
    while leftPtr < rightPtr:
        if numString[leftPtr] != numString[rightPtr]:
            return False
        leftPtr += 1
        rightPtr -= 1
            
    return True


# Time Complexity : O(n)
