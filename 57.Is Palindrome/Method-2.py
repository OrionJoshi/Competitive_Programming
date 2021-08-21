# Method-2 Using string reverse

def isPalindrome(num):
    numString = str(num)
    reverseNum = numString[::-1]

    return True if numString == reverseNum else False


# Time Complexity : O(n)