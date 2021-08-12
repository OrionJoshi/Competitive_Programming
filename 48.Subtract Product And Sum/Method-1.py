# Method-1

def subtractProductAndSum(n):
  totalSum = 0
  product = 1
  
  while n != 0:
      rem = n % 10
      product *= rem
      totalSum += rem
      n = int(n / 10)
      
  return product - totalSum

# Time Complexity : O(n)
# Space Complexity : O(1)