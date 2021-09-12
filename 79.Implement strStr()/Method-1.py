# Method-1

def strStr(haystack, needle):
    if needle == '':
        return 0
    if haystack == '':
        return -1
    
    needleLen = len(needle)
    haystackLen = len(haystack)
    
    ptr1 = 0
    ptr2 = 0
    
    while(ptr2 < haystackLen):
        if haystack[ptr2] == needle[ptr1]:
            if needle == haystack[ptr2: ptr2 + needleLen]:
                return ptr2
        ptr2 += 1
        
    return -1

# Time Complexity : O(n)
# Space Complexity : O(1)

# Input: haystack = "hello", needle = "ll"
# Output: 2