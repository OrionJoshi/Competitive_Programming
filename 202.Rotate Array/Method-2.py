# Method-2 

def rotate(nums, k):
  if k == 0:
      return nums

  k %= len(nums)
  count = 0
  start = 0
  while count < len(nums):
    curr = start
    prev = nums[start]
    
    while True:
      nxt = (curr + k) % len(nums)
      temp = nums[nxt]
      nums[nxt] = prev
      prev = temp
      curr = nxt
      count += 1
      
      if start == curr:
        break
        
    start += 1
      
  return nums

# Time Complexity : O(n)
# Space Complexity : O(1)