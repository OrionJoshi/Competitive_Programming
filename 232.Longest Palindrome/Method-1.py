# Method-1

from collections import Counter

def longestPalindrome(s):
    maxLen = 0
    mapping = Counter(s)
    oddFound = False
    for num in mapping.values():
        maxLen += (num // 2) * 2

        if num % 2 == 1:
            oddFound = True
    if oddFound:
        maxLen += 1

    return maxLen

# Time Complexity : O(n)
# Space Complexity : O(n)