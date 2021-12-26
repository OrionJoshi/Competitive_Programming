# Method-1

def firstPalindrome(words):
    length = len(words)
    
    for i in range(length):
        if words[i] == words[i][::-1]:
            return words[i]
            
    return ''

# Time Complexity : O(n * m)
# Space Complexity : O(1)