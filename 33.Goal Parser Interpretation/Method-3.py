# Method-3 Using Hashing

def goalParser(command):
    mapping = {
        'G': 'G',
        '()': 'o',
        '(al)': 'al'
    }
    temp = ''
    result = ''
    
    for char in command:
        temp += char
        if temp in mapping:
            result += mapping[temp]
            temp = ''
    return result

# Time Complexity : O(n)
# Space Complexty : O(1)