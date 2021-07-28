# Method-2

def goalParser(command):
    return command.replace('()', 'o').replace('(', '').replace(')', '')

# Time Complexity : O(n)
# Space Complexty : O(1)