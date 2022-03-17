# Method-1

def isIsomorphic(s, t):
    dictionary = {}
    
    for index, char in enumerate(s):
        
        if char not in dictionary:
            if t[index] in dictionary.values():
                return False
            else:
                dictionary[char] = t[index]
                
        else:
            if dictionary[char] != t[index]:
                return False
            
    return True

# Time Complexity : O(n)
# Space Complexity : O(n)