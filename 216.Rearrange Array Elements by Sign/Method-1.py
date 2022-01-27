# Method-1

def rearrangeArray(nums):
    evenPos = 0
    oddPos = 1
    result = [0 for i in range(len(nums))]

    for i in range(len(nums)):
        if nums[i] > 0:
            result[evenPos] = nums[i]
            evenPos += 2
        else:
            result[oddPos] = nums[i]
            oddPos += 2

    return result

# Time Complexity : O(n)
# Space Complexity : O(n)