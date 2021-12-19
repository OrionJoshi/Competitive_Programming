# Method-1

def canMakeArithmeticProgression(arr):
    arr.sort()
    difference = arr[1] - arr[0]

    for i in range(1, len(arr) - 1):
        if (arr[i + 1] - arr[i]) != difference:
            return False
    return True

# Time Complexity : O(nlogn)
# Space Complexity : O(1)