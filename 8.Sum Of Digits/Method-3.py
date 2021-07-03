# Method-3 Using num as string

def sumOfDigits(num):
    sum = 0
    for x in num:
        sum += int(x)
        
    return sum
    
print(sumOfDigits('123'))

# Time Complexity : O(n)
# Space Complexity : O(1)