# Method-1

def canJump(nums):
    m = 0

    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i + n)

    return True

# Time Complexity : O(n)
# Space Complexity: O(1)