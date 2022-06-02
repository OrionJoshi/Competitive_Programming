# Method-1

def dailyTemperatures(temperatures):
    res, stack = [0] * len(temperatures), []
    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            res[stack.pop()] = i - stack[-1]
        stack.append(i)

    return res

# Time Complexity : O(n)
# Space Complexity : O(n)