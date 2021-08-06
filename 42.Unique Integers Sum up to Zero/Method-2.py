# Method-2 list comprehension

def sumUpToZero(num):
    n = int(num/2)
    return [-i for i in range(-n , n + 1) if i!= 0 or num % 2 != 0]

# Time Complexity : O(n)
# Space Complexity : O(1)