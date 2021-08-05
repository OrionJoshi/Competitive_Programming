# Method-1 

def defangingIPAddress(ipAddress):
    to_replace = '.'
    replaced = '[.]'
    # Replace a character in string using for loop
    new_string = ''
    for elem in ipAddress:
        if elem == to_replace:
            new_string += replaced
        else:
            new_string += elem
    return new_string
    
# Time Complexity : O(n)