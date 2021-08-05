# Method-2

def evenNoOfDigits(lst):
   return  sum(len(str(x)) % 2 == 0 for x in lst)
   
# Time complexity : O(n)
# Space Complexity : O(1)