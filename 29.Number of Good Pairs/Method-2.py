# Method-2 Using Hashing

def noOfGoodPairs(lst):
    nums = {}  #empty hash
    count = 0
    for x in lst:
        if x in nums:
            count += 1
            nums[x] += 1
        else:
            nums[x] = 1
    return count

# Time Complexity : O(n)
# Space Complexity : O(n)