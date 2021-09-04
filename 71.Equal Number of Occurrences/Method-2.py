# Method-2 Using Counter

from collections import Counter
def areOccurencesEqual(s):
    mapping = Counter(s)
    return len(set((mapping.values()))) == 1

# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

# Time Complexity : O(n)
# Space Complexity : O(n)
