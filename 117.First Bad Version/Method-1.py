# Method-1 Binary Search

def firstBadVersion(self, n):

    left = 1
    right = n
    
    while left < right:
        mid = (left + right) // 2
        if(isBadVersion(mid)):
            right = mid
        else:
            left = mid + 1
    return left

# Time Complexity : O(logn)
# Space Complexity : O(1)

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.