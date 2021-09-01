# Method-1 Using pointers

def reverseString(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Time Complexity : O(n)
# Space Complexity : O(1)