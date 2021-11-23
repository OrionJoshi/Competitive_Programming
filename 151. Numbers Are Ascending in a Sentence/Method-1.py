# Method-1 

def areNumbersAscending(s):
    n = 0
    for i in s.split():
        if i.isdigit():
            if int(i) <= n:
                return False
            n = int(i)
    return True

# Time Complexity : O(n)
# Space Complexity : O(1)