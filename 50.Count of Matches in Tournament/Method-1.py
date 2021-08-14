# Method-1

def numberOfMatches(n):
    totalMatches = 0
    rem = 0
    
    while n != 1:
        totalMatches += n // 2
        rem = n % 2
        n = n // 2 + rem
    return totalMatches
    
# Time Complexity : O(logn)
# Space Complexity : O(1)