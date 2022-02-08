# Method-1 Hash Table

def subarraySum(nums, k):
    count = 0
    currSum = 0
    mapping = {0 : 1}

    for num in nums:
        currSum += num
        diff = currSum - k
        count += mapping.get(diff, 0)
        if currSum in mapping:
            mapping[currSum] += 1
        else:
            mapping[currSum] = 1

    return count

# Time Complexity : O(n)
# Space Complexity : O(n)