# Method-3: Two Pointer variables

def twoNumberSum(array, target):
    array.sort()
    left = 0
    right = len(array) - 1
    while(left < right):
        currentSum = array[left] + array[right]
        if(currentSum == target):
            return [array[left], array[right]]
        elif(currentSum < target):
            left += 1
        elif(currentSum > target):
            right -= 1

    return []

a = [1,2,3,4,5]
target = 5

result = twoNumberSum(a,target)

if(result):
    print(result)
else:
    print("There are no elements whose sum is {}".format(target))


# Time Complexity: O(nlogn)
# Space Complexity: O(1)