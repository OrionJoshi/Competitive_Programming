# Method-2 Hash Table

def twoSum2(numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1]
        dic[num] = i

# Time Complexity : O(n)
# Space Complexity : O(n)