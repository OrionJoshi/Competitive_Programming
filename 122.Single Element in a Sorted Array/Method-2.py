# Method-2 Using Set

def singleNonDuplicate(nums):
    return 2 * sum(set(nums)) - sum(nums)

# Time Complexity : O(n)
# Space Complexity : O(1)