# Method-1

def validPalindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            str1 = s[:left] + s[left + 1:]
            str2 = s[:right] + s[right + 1:]
            
            return str1 == str1[::-1] or str2 == str2[::-1]
        
        left += 1
        right -= 1
        
    return True

# Time Complexity : O(n)
# Space Complexity : O(n)