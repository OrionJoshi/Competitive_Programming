# Method-1

def sortColors(nums):
    countRed = 0
    countWhite = 0
    countBlue = 0

    for obj in nums:
        if obj == 0:
            countRed += 1
        elif obj == 1:
            countWhite += 1
        else:
            countBlue += 1

    for i in range(len(nums)):
        if countRed:
            nums[i] = 0
            countRed -= 1
        elif countWhite:
            nums[i] = 1
            countWhite -= 1
        else:
            nums[i] = 2
            countBlue -= 1

# Time Complexity : O(n)
# Space Complexity : O(1)