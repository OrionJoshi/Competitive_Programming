# Method-1

def subtractProductAndSum(n):
  totalSum = 0
  product = 1
  for i in str(n):
      product *= int(i)
      totalSum += int(i)
      
  return product - totalSum

# Time Complexity : O(n)
# Space Complexity : O(1)