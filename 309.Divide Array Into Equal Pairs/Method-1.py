# Method-1

from collections import Counter

def divideArray(nums):
    length = len(nums)
    count = sum(num//2 for num in Counter(nums).values())
    return (length/2 == count)

# Time Complexity : O(n)
# Space Complexity : O(1)