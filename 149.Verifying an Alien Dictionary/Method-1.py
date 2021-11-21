# Method-1

def isAlienSorted(words, order):
    wordLen = len(words)
    mapping = {}
    
    for index, val in enumerate(order):
        mapping[val] = index
        
    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            if j >= len(words[i + 1]): 
                return False
            if words[i][j] != words[i + 1][j]:
                if mapping[words[i][j]] > mapping[words[i + 1][j]]:
                    return False
                break
                    
    return True

# Time Complexity : O(NxM) 
# Space Complexity : O(1)
# where, N is the number of words
# and M is length of the individual words.