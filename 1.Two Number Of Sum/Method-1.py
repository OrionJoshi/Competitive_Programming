# method 1: Brute Force Method

# function definition
def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if(firstNum + secondNum == targetSum):
                return [firstNum, secondNum]
    return []

a = [1,2,3,4,5]
target = 5

result = twoNumberSum(a,target)

if(result):
    print(result)
else:
    print("There are no elements whose sum is {}".format(target))

# time Complexity:  O(n^2)
# Space Complexity: O(1)
