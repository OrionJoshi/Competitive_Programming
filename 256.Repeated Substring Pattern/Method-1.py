# Method-1

def repeatedSubstringPattern(s):

    for i in range(1, (len(s) // 2) + 1):
        if s[:i] * (len(s) // i) == s:
            return True

    return False

# Time Complexity : O(n)
# Space Complexity : O(1)