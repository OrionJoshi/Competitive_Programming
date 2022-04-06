# Method-1

def maxSubsequence(nums, k):
    result = []

    for i,j in enumerate(nums):
        if len(result)==k:
            heappushpop(result,(j,i))
        else:
            heappush(result,(j,i))
    ans = []
    result.sort(key=lambda x:x[1])
    for i in result:
        ans.append(i[0])
    return ans

# Time Complexity : O(nlogn)
# Space Complexity : O(n)