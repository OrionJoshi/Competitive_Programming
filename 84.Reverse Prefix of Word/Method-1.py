# Method-1 Using pointers

def reversePrefix(word, ch):
    length = len(word)
    ptr1 = 0
    ptr2 = 0
    
    result = ''
    
    while ptr2 < length:
        if word[ptr2] == ch:
            break
        ptr2 += 1
        
    if ptr2 == length:
        return word
    else:
        ptr1 = ptr2
        while ptr1 >= 0:
            result += word[ptr1]
            ptr1 -= 1
    return result + word[ptr2 + 1: length]

# Time Complexity : O(n)
# Space Complexity : O(n)
    