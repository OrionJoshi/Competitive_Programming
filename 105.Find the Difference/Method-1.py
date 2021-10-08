# Method-1

def findTheDifference(s, t):
    sum1 = 0
    sum2 = 0
    
    for char in s:
        sum1 += ord(char)
    for char in t:
        sum2 += ord(char)
        
    return chr(sum2 - sum1)

# Time Complexity : O(n)
# Space Complexity : O(1)

# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.