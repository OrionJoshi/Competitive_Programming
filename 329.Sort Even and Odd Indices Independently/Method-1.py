# Method-1

def sortEvenOdd(nums):
    n = len(nums)
    if n <= 2:
        return nums

    even = sorted([nums[i] for i in range(0, n, 2)])
    odd = sorted([nums[i] for i in range(1, n, 2)], reverse=True)

    res = []

    for i in range(len(even)):
        res.append(even[i])
        if i < len(odd):
            res.append(odd[i])

    return res

# Time Complexity : O(nlogn)
# Space Complexity : O(n)