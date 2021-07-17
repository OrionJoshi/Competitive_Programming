# Method-1 Using split method

def lenOfLastWord(str):
    lst = str.split()
    if len(lst) == 0:
        return 0
    else:
        lenOfWord = len(lst[-1])
        return lenOfWord

# Time Complexity : O(n)
# Space Complexity : O(n)