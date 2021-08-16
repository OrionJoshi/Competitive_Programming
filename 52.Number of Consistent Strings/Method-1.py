# Method-1

def countConsistentStrings(allowed, words):
    length = len(words)
    mapping = {}
    count = 0
    
    for char in allowed:
        mapping[char] = 1
        
    for string in words:
        for letter in string:
            if letter not in mapping:
                break
        else:
            count += 1
            
    return count
    
# Time Complexity : O(n * m)
# Space Complexity : O(k),
# n = nos of words
# m = maximum lenght of word
# k = lenght of allowed