# Method-2 Using pointers

def threeConsecutiveOdds(lst):
    oddCount = 0
    length = len(lst)
    
    for i in range(0, length - 2):
        one = i
        two = i + 1
        three = i + 2
        
        if lst[one] % 2 != 0 and lst[two] % 2 != 0 and lst[three] % 2 != 0:
            return True
            
    return False

# Time Complexity : O(n)
# Space Complexity : O(1)