# Method-2 Using pointers

def reverseOnlyLetters(s):
    lst = [x for x in s]
    
    ptr1 = 0
    ptr2 = len(lst) - 1
    
    while ptr1 < ptr2:
        if lst[ptr1].isalpha() and lst[ptr2].isalpha():
            lst[ptr1], lst[ptr2] = lst[ptr2], lst[ptr1]
            ptr1 += 1
            ptr2 -= 1
        else:
            if lst[ptr1].isalpha():
                ptr2 -= 1
            else:
                ptr1 += 1
    return "".join(lst)

# Time Complexity :  O(n)
# Space Complexity : O(n)