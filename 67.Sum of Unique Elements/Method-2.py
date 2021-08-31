# Method-2

def sumOfUnique(nums):
    totalSum = 0
    
    for num in nums:
        if nums.count(num) == 1:
            totalSum += num

    return totalSum

# Time Complexity : O(n * n)
# (due to count method inside loop)
# Space Complexity : O(1)
        