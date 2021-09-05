# Method-2 Using set() function

def areAnagram(str1, str2):
    return True if set(str1.lower()) == set(str2.lower()) else False

# Time Complexity : O(n)
# Space Complexity : O(1)