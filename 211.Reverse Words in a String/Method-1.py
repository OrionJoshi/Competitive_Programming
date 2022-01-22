# Method-1 Using pointers

def reverseWords(s):
    result, i = '', len(s) - 1

    while i >= 0:
        while i >= 0 and s[i] == ' ':
            i -= 1
        j = i - 1
        while j >= 0 and s[j] != ' ':
            j -= 1
        if i < 0:
            break
        subString = s[j + 1:i + 1]
        if len(result) == 0:
            result = subString
        else:
            result = result + ' ' + subString
        i = j - 1

    return result

# Time Complexity : O(n)
# Space Complexity : O(n)