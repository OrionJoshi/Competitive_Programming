# Method-1

def targetIndices(nums,target):
    smaller = 0
    numOccurence = 0
    
    for i in range(len(nums)):
        if nums[i] < target:
            smaller += 1
        elif nums[i] == target:
            numOccurence += 1
    return list(range(smaller, smaller+numOccurence))

# Time Complexity : O(n)
# Space Complexity : O(1)