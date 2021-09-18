# Method-1 Using Stack

def reverseOnlyLetters(s):
    letters = [x for x in s if x.isalpha()]
    result = []
    
    for ch in s:
        if ch.isalpha():
            result.append(letters.pop())
        else:
            result.append(ch)
    return "".join(result)

# Time Complexity :  O(n)
# Space Complexity : O(n + m)