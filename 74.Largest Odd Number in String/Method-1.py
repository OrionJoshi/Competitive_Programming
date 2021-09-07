# Method-1

def largestOddNumber(num):
    length = len(num)
    oddList = ['1','3','5','7','9']
    
    for i in range(length - 1, -1, -1):
        if num[i] in oddList:
            return num[:i + 1]
    return ""

# Time Complexity : O(n)
# Space Complexity : O(1)

# Input: num = "52"
# Output: "5"
# Explanation: The only non-empty substrings are
#  "5", "2", and "52". "5" is the only odd number.