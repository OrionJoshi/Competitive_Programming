def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1 , len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        swap(smallestIdx, currentIdx,array)
        currentIdx += 1

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

# Time Complexity:  O(n^2)
# Space Complexity: O(1)