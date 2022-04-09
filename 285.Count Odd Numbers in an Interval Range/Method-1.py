# Method-1

def countOdds(low, high):
    noOfElement = high - low + 1
    
    if low % 2 != 0 and high % 2 != 0:
        result = noOfElement // 2 + 1
    else:
        result = noOfElement // 2
        
    return result

# Time Complexity : O(1)
# Space Complexity : O(1)