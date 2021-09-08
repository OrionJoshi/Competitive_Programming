# Method-2 Using Pointers

def reverseWords(s):

    lst = []
    length = len(s)
    
    ptr1 = 0
    ptr2 = 0
    
    while(ptr2 < length):
        if s[ptr2] == ' ':
            lst.append(s[ptr1:ptr2][::-1])
            ptr1 = ptr2 + 1
            ptr2 += 1
        else:
            ptr2 += 1
    lst.append(s[ptr1:ptr2][::-1])
    return (' '.join(lst))

# Time Complexity : O(n)
# Space Complexity : O(n)

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"