# Method-2 Using List comprehension

def greatestNoCandies(candies, extra):
    # finding maximum
    maxNoCandies = max(candies)
    
    return [(x+extra) >= maxNoCandies  for x in candies]
    
# Time Complexity : O(n)
# Space Complexity : O(n)  