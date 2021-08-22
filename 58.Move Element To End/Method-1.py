# Method-1: Using pointer Variables

def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            swap(array, i, j)
        i += 1
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

# Time Compexity:   O(n)
# Space Complexity: O(1)