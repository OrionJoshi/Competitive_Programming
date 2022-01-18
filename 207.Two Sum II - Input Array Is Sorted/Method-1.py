# Method-1 Using Pointer

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        currSum = numbers[left] + numbers[right]
        if currSum == target:
            return [left + 1, right + 1]
        elif currSum > target:
            right -= 1
        else:
            left += 1
    return []

# Time Complexity : O(n)
# Space Complexity : O(1)