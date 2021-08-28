# Method-1 

def sortArrayByParity(nums):
    return [num for num in nums if num % 2 == 0] + [num for num in nums if num % 2 == 1]


# Time Complexity: O(n)
# Space Complexity: O(n)