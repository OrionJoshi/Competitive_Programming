# Method-1

def numberOfSteps(num):
    count = 0
    while num:
        if num % 2:
            num -= 1
        else:
            num /= 2
        count += 1
        
    return count

# Time Complexity : O(logN)
# Space Complexity : O(1)