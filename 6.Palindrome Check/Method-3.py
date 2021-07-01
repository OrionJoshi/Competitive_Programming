# Method-3: Recursive Solution

def isPalindrome(string, i = 0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)


# Time Complexity:  O(n)
# Space Complexity: O(n)
