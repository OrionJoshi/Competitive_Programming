# Method-1

def countOperations(num1, num2):
    count = 0
    
    while True:
        if num1 == 0 or num2 == 0:
            return count
            
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1

# Time Complexity : O(m)
# Space Complexity : O(1)