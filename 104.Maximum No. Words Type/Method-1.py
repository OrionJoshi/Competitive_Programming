# Method-1

def canBeTypedWords(text, brokenLetters):
    t = set(brokenLetters)
    count = 0
    
    for word in text.split():
        for char in word:
            if char in t:
                break
        else:
            count += 1
        
    return count

# Time Complexity : O(n * m)
# Space Complexity : O(m)
# where n = lenght of text
# and m = length of brokenLetters

# Input: text = "hello world",
#  brokenLetters = "ad"
# Output: 1
# Explanation: We cannot type "world"
#  because the 'd' key is broken.