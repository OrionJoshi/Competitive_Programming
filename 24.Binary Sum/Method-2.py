# Method-2 using functions

def binarySum(a, b):
  num1 = int(a, 2)
  num2 = int(b, 2)
  return bin(num1 + num2)[2:]

# Time Complexity : O(n)
# Space Complexity : O(1)

