# Method-2

def maximum69Number(num):
    result = ''
    string = str(num)
    flag = True
    
    for x in string:
        if x == '6' and flag:
            flag = False
            result += '9'
        else:
            result += x
            
    return int(result)

# Time Complexity : O(n)
# Space Complexity : O(n)
# where n is the no of digits
    