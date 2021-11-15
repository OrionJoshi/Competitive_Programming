# Method-2 Using Hash table

def findDuplicates(nums):
    mapping = {}
    lenght = len(nums)
    
    for i in range(lenght):
        if nums[i] not in mapping:
            mapping[nums[i]] = 1
        else:
            mapping[nums[i]] += 1
    return [x for x in mapping if mapping[x] == 2]

# Time Complexity : O(n)
# Space Complexity : O(n)
