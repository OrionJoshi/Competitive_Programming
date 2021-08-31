# Method-1

def sumOfUnique(nums):
    mapping = {}
    totalSum = 0
    
    for num in nums:
        if num not in mapping:
            mapping[num] = 1
        else:
            mapping[num] += 1
            
    for num in mapping:
        if mapping[num] == 1:
            totalSum += num
            
    return totalSum

# Time Complexity : O(n)
# Space Complexity : O(n)
