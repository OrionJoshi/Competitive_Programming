# Method-1

def checkArithmeticSubarrays(nums, l, r):
    res = []

    for i in range(len(l)):
        subarr = sorted(nums[l[i] : r[i] + 1])
        diff = [subarr[j+1] - subarr[j] for j in range(len(subarr) - 1)]

        if len(set(diff)) == 1:
            res.append(True)
        else:
            res.append(False)
            
    return res

# Time Complexity : O(nlogn)
# Space Complexity : O(n)