# Method-1

from collections import deque
def plusOne(digits):
    num = 1
    i = 0 
    for d in reversed(digits):
        num += d * pow(10, i)
        i += 1
    new = deque()
    while num:
        num,r = divmod(num,10)
        new.appendleft(r)
    return new
    

# Time complexity : O(n)
# Space Complexity : O(n)