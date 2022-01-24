# Method-2 Hash Table

def findDisappearedNumbers(nums):
    result = []
    mapping = {}

    for num in nums:
        if num not in mapping:
            mapping[num] = True
    for i in range(1, len(nums) + 1):
        if i not in mapping:
            result.append(i)

    return result

# Time Complexity : O(n)
# Space Complexity : O(n)