# Method-1 Using Hash table

def wordPattern(pattern, s):
    mapping = {}

    if len(pattern) != len(s.split()):
        return False
    
    for i, word in enumerate(s.split()):

        if pattern[i] not in mapping:
            if word not in mapping.values():
                mapping[pattern[i]] = word
            else:
                return False
        else:
          
            if mapping[pattern[i]] != word:
                return False
                
    return True

# Time Complexity : O(n)
# Space Complexity : O(n)