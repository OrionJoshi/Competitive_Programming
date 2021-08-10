# Method-1

def largestAltitude(gain): 
    lst = [0]
    
    for alt in gain:
        currentElemLst = lst[-1]
        lst.append(alt + currentElemLst)
        
    return max(lst)

# Time Complexity : O(n)
# Space Complexity : O(1)