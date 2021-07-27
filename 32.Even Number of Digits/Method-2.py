# Method-2: Using String len function

def evenNoOfDigits(lst):
   return  sum(len(str(x)) % 2 == 0 for x in lst)

# Time Complexity : O(n)
# Space Complexity : O(1)