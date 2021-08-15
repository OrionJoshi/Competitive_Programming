# Method-1

def maximum69Number(num):

    index = 0
    string = str(num)
    index = string.index('6') if '6' in string else 0
    string = string[:index] + '9' + string[index + 1:]
    
    return int(string)

# Time Complexity : O(n)
# Space Complexity : O(n)
# where n is the no of digits