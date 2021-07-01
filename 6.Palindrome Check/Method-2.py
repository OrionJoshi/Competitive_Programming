# Method-2: Using List

def isPalindrome(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])   # Takes O(1) time complexity
    return "".join(reversedChars) == string

# Time Complexity:  O(n)
# Space Complexity: O(n) 
