# Method-1

def sentenceIsPangram(sentence):
    return True if len(set(sentence)) == 26 else False
    
# Time Complexity : O(n)
# Space Complexity : O(1)