# Method-1: Using reverse string

def isPalindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]         # Takes O(n) time complexity
    return string == reversedString

# Time Complexity : O(n^2)
# Space Complexity: O(n)