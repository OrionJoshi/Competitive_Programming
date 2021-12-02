# Method-1

def findPoisonedDuration(timeSeries, duration):
    length = len(timeSeries)
    second = 0

    for i in range(length - 1):

        if (timeSeries[i] + duration) > timeSeries[i + 1]:
            second += timeSeries[i + 1] - timeSeries[i]
        else:
            second += duration

    return second + duration

# Time Complexity : O(n)
# Space Complexity : O(1)