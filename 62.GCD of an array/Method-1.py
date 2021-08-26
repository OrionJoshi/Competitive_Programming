# Method-1 Using euclidean algorithm

def findGCD(nums):
    largestVal = max(nums)
    smallestVal = min(nums)
    
    return gcd(largestVal, smallestVal)
    
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Time Complexity : O(log n)
# Space Complexity : O(log n)