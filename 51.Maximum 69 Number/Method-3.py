# Method-3

from math import*
def maximum69Number(num):
    result = 0
    noOfDigits = floor(log10(num)) + 1
    flag = True
    
    while noOfDigits:

        currentDigit = (int(num // pow(10, noOfDigits - 1))) % 10
        if currentDigit == 6 and flag:
            flag = False
            result = result + 9 * pow(10, noOfDigits - 1)
        else:
             result = result + currentDigit * pow(10, noOfDigits - 1)
             
        noOfDigits -= 1
    return int(result)
  
# Time Complexity : O(n)
# Space Complexity : O(1)