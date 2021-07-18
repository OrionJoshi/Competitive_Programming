# Method-3  Using Hashing
def singleNum(lst):
    nums = {} # empty hash
    for x in lst:
        if x in nums:
            nums[x] += 1
        else:
            nums[x] = 1
            
    for num in nums:
        if nums[num] == 1:
            return num

# Time Complexity : O(n)
# Space Complexity : O(n)
         