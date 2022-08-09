# Method-1

def numberOfArrays(differences, lower, upper):
    pfix = minimum = maximum = 0 
    
    for x in differences: 
        pfix += x
        minimum = min(minimum, pfix)
        maximum = max(maximum, pfix)
        
    return max(0, (upper - lower) - (maximum - minimum) + 1)

# Time Complexity : O(n)
# Space Complexity : O(1)