# Method-1 Iterative method

def noOfGoodPairs(lst):
    count = 0
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length):
            if lst[i] == lst[j]:
                count += 1
    return count

print(noOfGoodPairs([1,2,3]))

# Time Complexity : O(n^2)
# Space Complexity : O(1)
        