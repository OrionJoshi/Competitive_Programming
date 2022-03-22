# Method-1

def isPalindrome(s):
  s = [i for i in s.lower() if i.isalnum()]
  return s == s[::-1]

# Time Complexity : O(n)
# Space Complexity : O(n)