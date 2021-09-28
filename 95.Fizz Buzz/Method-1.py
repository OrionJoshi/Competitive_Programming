# Method-1

def fizzBuzz(n):
    result = []
    
    for i in range(n):
        num = i + 1
        isDivisibleBy3 = num % 3 == 0
        isDivisibleBy5 = num % 5 == 0
        
        if isDivisibleBy3 and isDivisibleBy5:
            result.append('FizzBuzz')
        elif isDivisibleBy3:
            result.append('Fizz')
        elif isDivisibleBy5:
            result.append('Buzz')
        else:
            result.append(num)
            
    return result

# Time Complexity : O(n)
# Space Complexity : O(n)

# Input: n = 3
# Output: ["1","2","Fizz"]