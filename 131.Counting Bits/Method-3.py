# Method-3 List comprehension
 
def countBits(n):
    return [("{0:b}".format(int(i))).count('1') for i in range(n + 1)]

# Time Complexity : O(nlogn)
# Space Complexity : O(1)