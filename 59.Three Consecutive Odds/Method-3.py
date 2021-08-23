# Method-3 Using String

def threeConsecutiveOdds(arr):
    return str([i & 1 for i in arr]).find('1, 1, 1') > 0

# Time Complexity : O(n)
# Space Complexity : O(1)