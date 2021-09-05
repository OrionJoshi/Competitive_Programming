# Method-1 Using Sorted function

def areAnagram(str1, str2):
  if sorted(str1) == sorted(str2):
    return True
  else:
    return False 

# Time Complexity : O(nlogn)
# Space Complexity : O(1)