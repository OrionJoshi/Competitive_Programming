# Method-3

from math import*
def evenNoOfDigits(nums):
    totalNum = 0
    for num in nums:
        if (floor(log10(num)) + 1) % 2 == 0:
            totalNum += 1
    return totalNum

# Time complexity : O(n)
# Space Complexity : O(1)