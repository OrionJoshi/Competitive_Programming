# Method-2 Recursion Method

def sumOfDigits(num, sum = 0):
    
    if(num == 0):
        return sum
    else:
        sum += num % 10
        num = int(num / 10)
        return sumOfDigits(num, sum)
    

num = int(123)
print(sumOfDigits(num))

# Time Complexity : O(log10(n))
# Space Complexity : O(log10(n))