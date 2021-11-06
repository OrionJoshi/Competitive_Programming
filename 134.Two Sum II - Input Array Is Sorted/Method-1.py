# Method-1 Pointer

def twoSum1(numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1

# Time Complexity : O(n)
# Space Complexity : O(1)