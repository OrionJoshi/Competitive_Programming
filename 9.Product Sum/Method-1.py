# Method-1 Recursive call

def productSum(array, multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier
    
l = [5,2,[7,-1],3,[6,[-13,8],4]]

result = productSum(l)

print("The product Sum of given special list is : {}".format(result))


# Time Complexity: O(N), Where N = Total number of elements in array(including the elements of subarray)
# Space Complexity: O(d), Where d = greatest depth of subarray