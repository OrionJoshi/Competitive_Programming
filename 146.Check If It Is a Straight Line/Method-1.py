# Method-1 Math

def checkStraightLine(coordinates):
  length = len(coordinates)
  
  if length == 2:
      return True
  
  dy = coordinates[1][1] - coordinates[0][1]
  dx = coordinates[1][0] - coordinates[0][0]
  
  for i in range(2, length):
      d2y = coordinates[i][1] - coordinates[i - 1][1]
      d2x = coordinates[i][0] - coordinates[i - 1][0]
      if (dy * d2x) != (d2y * dx):
          return False
          
  return True

# Time Complexity : O(n)
# Space Complexity : O(1)