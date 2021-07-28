# Method-1 

def goalParser(command):
  newStr = command.replace('()', 'o')
  chars = '()'

  for char in chars:
      newStr = newStr.replace(char, '')
      
  return newStr

# Time Complexity : O(n)
# Space Complexty : O(1)

