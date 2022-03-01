# Method-1

def findMaxConsecutiveOnes(nums):
    c1, c2 = 0, 0

    for i in nums:
        if i == 1:
            c1 += 1
        elif i == 0:
            c1 = 0
        if c1 > c2:
            c2 = c1

    return c2

# Time Complexity : O(n)
# Space Complexity : O(1)