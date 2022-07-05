# Method-1

def lengthOfLongestSubstring(s):
    string = s
    max_length = 0
    seen_character = ''
    
    for letter in string:
        if letter not in seen_character:
            seen_character += letter 
        else:
            seen_character = seen_character[seen_character.index(letter) + 1:] + letter       
            
        max_length = max(max_length, len(seen_character))
        
    return max_length

# Time Complexity : O(n)
# Space Complexity : O(n)