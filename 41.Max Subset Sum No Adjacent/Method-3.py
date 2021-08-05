# Method-3:

def MaxSubsetSumNoAdjacent(array):
    if not len(array):
        return -1
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first

# Time Complexity:  O(n)
# Space Complexity: O(1)