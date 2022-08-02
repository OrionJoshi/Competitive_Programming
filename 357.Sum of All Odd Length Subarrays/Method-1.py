# Method-1

def sumOddLengthSubarrays(arr):
    s=0

    for i in range(len(arr)):
        for j in range(i,len(arr),2):
            s+=sum(arr[i:j+1])

    return s

# Time Complexity : O(n^2)
# Space Complexity : O(1)