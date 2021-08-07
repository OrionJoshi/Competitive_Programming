# Method-2

def sentenceIsPangram(sentence):
    dic = {} # empty dictionary
    
    for char in sentence:
        if char not in dic:
            dic[char] = 1
            
    return True if len(dic) == 26 else False

# Time Complexity : O(n)
# Space Complexity : O(1)