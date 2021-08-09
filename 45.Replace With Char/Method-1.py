# Method-1

def replaceWithChar(s):
    length = len(s)
    result = ''
    
    for i in range(0, length, 2):
        result += s[i]
        if i + 1 < length:
            character = chr(ord(s[i]) + int(s[i + 1]))
            result += character
        
    return result

# Time Complexity : O(n)
# Space Complexity : O(1)