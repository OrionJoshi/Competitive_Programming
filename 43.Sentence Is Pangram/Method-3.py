# Method-3

def sentenceIsPangram(sentence):
    result = 0
    ans  = sum(i for i in range(97, 123))
    
    for char in set(sentence):
        result += ord(char)
    
    return True if ans == result else False

# Time Complexity : O(n)
# Space Complexity : O(1)