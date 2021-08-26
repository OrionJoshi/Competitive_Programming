# Method-3 Using Iterative method

def findGCD(nums):
    
    largestVal = max(nums)
    smallestVal = min(nums)
    
    for i in range(1,smallestVal + 1):
        if (smallestVal % i == 0 and largestVal % i == 0):
            gcd = i
            
    return gcd

# Time Complexity : O(n),
# Where n = numbers in list (due to max and min function)
# Space Complexity : O(1)