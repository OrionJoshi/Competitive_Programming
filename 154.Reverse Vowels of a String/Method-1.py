# Method-1 Using Pointer

def reverseVowels(s):
    vowel = set(list('aeiouAEIOU'))
    lst = list(s)
    
    ptr1 = 0
    ptr2 = len(s) - 1
    
    while ptr1 < ptr2:
        if lst[ptr1] in vowel and lst[ptr2] in vowel:
            lst[ptr1], lst[ptr2] = lst[ptr2], lst[ptr1]
            ptr1 += 1
            ptr2 -= 1
            
        if lst[ptr1] not in vowel:
            ptr1 += 1
        if lst[ptr2] not in vowel:
            ptr2 -= 1
            
    return ''.join(lst)

# Time Complexity : O(n)
# Space Complexity : O(n)

# Input: s = "hello"
# Output: "holle"