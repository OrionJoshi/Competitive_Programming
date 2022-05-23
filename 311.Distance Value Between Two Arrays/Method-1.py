# Method-1

def findTheDistanceValue(arr1, arr2, d):
    res = len(arr1)
    for i in arr1:
        for j in arr2:
            if(abs(i - j) > d):
                continue
            else:
                res-=1
                break
    return res

# Time Complexity : O(n^2)
# Space Complexity : O(1)
