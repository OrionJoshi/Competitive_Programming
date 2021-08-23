# Method-1 Iterative

def threeConsecutiveOdds(lst):
    oddCount = 0
    length = len(lst)
    
    for i in range(0, length - 2):
        if lst[i] % 2 == 0:
            oddCount = 0
        else:
            oddCount += 1
            
        if oddCount == 3:
            return True
            
    return False

# Time Complexity : O(n)
# Space Complexity : O(1)