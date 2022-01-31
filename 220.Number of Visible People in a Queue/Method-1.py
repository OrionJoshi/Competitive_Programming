# Method-1 Using Stack

def canSeePersonsCount(heights):
    ans = [0] * len(heights)
    stack = []

    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] <= height:
            ans[stack.pop()] += 1
        if stack:
            ans[stack[-1]] += 1
        stack.append(i)

    return ans

# Time Complexity : O(n)
# Space Complexity : O(n)