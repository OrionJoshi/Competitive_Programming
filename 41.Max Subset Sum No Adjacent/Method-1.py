# Method-1:

def MaxSubsetSumNoAdjacent(array):
    inc = array[0]
    exc = 0

    for i in range(1, len(array)):
        nextInc = exc + array[i]
        nextExc = max(inc, exc)

        inc = nextInc
        exc = nextExc

    return max(inc, exc)

# Time Complexity:  O(n)
# Space Complexity: O(1)