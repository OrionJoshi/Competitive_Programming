# Method-1 : Iterative Method

def SumOfDigits(num):
    num = int(num)
    sum = 0
    while num != 0:
        lastDigit = num % 10
        sum += lastDigit
        num = int(num / 10)
        
    return sum
    
inputNum = 120

print(SumOfDigits(inputNum))

# Time complexity : log10(N)
# Space Complexity : O(1)