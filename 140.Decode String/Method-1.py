# Method-1 Using Stack

def decodeString(s):
    length = len(s)
    stack = []
    
    for i in range(length):
        if s[i] != ']':
            stack.append(s[i])
        else:
            substr = ''
            while stack[-1] != '[':
                substr = stack.pop() + substr
            stack.pop()
            
            digit = ''
            while stack and stack[-1].isdigit():
                digit = stack.pop() + digit
            stack.append(int(digit) * substr )
    return ''.join(stack)
                
# Time and Space Complexity depends
# on the input