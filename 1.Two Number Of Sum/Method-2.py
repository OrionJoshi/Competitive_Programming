# Method-2: Hashing

def twoNumberSum(array, target):
    nums = {}  # Empty hash table

    for num in array:
        potentialMatch = target - num
        if(potentialMatch in nums):
            return [potentialMatch, num]
        else:
            nums[num] = True
    return[]

a = [1,2,3,4,5]
target = 5

result = twoNumberSum(a,target)

if(result):
    print(result)
else:
    print("There are no elements whose sum is {}".format(target))

# Time Complexity:  O(n)
# Space Complexity: O(n)