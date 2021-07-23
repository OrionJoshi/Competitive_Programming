# Method-1 Iterative Method
def greatestNoCandies(candies, extra):
    length = len(candies)
    
    # finding maximum
    maxNoCandies = max(candies)
    
    for i in range(length):
        if candies[i] + extra >= maxNoCandies:
            candies[i] = True
        else:
            candies[i] = False
            
    return candies
    
# Time Complexity : O(n)
# Space Complexity : O(1)
