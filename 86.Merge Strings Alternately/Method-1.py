# Method-1 Using pointers

def mergeAlternately(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    ptr = 0
    
    result = ['' for i in range(len1 + len2)]
    
    for i in range(len1):
        result[ptr] = word1[i]
        if i < len2:
            ptr += 2
        else:
            ptr += 1
        
    ptr = 1   
    
    for i in range(len2):
        result[ptr] = word2[i]
        
        if i < len1 - 1:
            ptr += 2
        else:
            ptr += 1
            
    return ''.join(result)  

# Time Complexity : O(n)
# Space Complexity : O(n)
# where n = len(word1) + len(word2)
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"