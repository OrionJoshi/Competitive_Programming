# Method-1 Using pointers

def arrayIntersection(arr1, arr2, arr3):
    i = 0
    j = 0
    k = 0
    result = []
    
    while(i < len(arr1) and j < len(arr2) and k < len(arr3)):
        if arr1[i] == arr2[j] and arr1[i] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
            i += 1
        elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]:
            j += 1
        else:
            k += 1
            
    return result

# Time Complexity : O(n)
# Space Complexity : O(m)

# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.