# Method-4: Tail Recursion

def isPalindrome(string, i = 0):
    j = len(string) - 1 - i
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome(string, i + 1)

# Time Complexity : O(n)
# Space Complexity: O(1)
