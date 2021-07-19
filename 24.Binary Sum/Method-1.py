# Method-1 

def binarySum(a,b):
    decimalNum1 = binaryToDecimal(a)
    decimalNum2 = binaryToDecimal(b)
    
    totalDecSum = decimalNum1 + decimalNum2
    
    return decimalToBinary(totalDecSum)
 
# convert binary num to decimal 
def binaryToDecimal(str):
    i = 0
    totalSum = 0
    for x in reversed(str):
        totalSum += int(x) * pow(2, i)
        i += 1
    return totalSum
    
# convert decimal to binary num
def decimalToBinary(decNum):
    return str(bin(decNum)[2:])

# Time Complexity : O(n)
# Space Complexity : O(1)