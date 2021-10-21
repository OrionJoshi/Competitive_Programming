# Method-1

def maxArea(height):
    length = len(height)

    ptr1 = 0
    ptr2 = length - 1
    width = length - 1
    area = 0

    while ptr1 < ptr2:
        tempArea = min(height[ptr1], height[ptr2]) * width

        if area < tempArea:
            area = tempArea

        if height[ptr1] < height[ptr2]:
            ptr1 += 1
        else:
            ptr2 -= 1

        width -= 1

    return area

# Time Complexity : O(n)
# Space Complexity : O(1)

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented
# by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section)
# the container can contain is 49.