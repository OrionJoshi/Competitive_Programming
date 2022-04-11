# Method-1

def areAlmostEqual(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    diffs = [i for i in range(len(s1)) if s1[i] != s2[i]]
    return len(diffs) == 2 and s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]]

# Time Complexity : O(n)
# Space Complexity : O(n)