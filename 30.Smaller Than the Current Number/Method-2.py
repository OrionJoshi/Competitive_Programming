# Method-2 Using Hashing

def smallerNumbers(lst):
    temp = sorted(lst)
    nums = {}  # empty hash
    length = len(lst)
    
    for i in range(length):
        if temp[i] not in nums:
            nums[temp[i]] = i
            
    for i in range(length):
        lst[i] = nums[lst[i]]
    
    return lst    

# Time complexity : O(nlogn)
# space Complexity : O(n)