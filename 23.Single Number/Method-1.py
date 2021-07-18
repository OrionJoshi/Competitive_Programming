# Method-1 Iterative Method

def singleNum(lst):
    lenOfNums = len(lst)
    for i in range(lenOfNums):
        single = lst[i]
        for j in range(lenOfNums):
            if i == j:
                continue
            else:
                if single == lst[j]:
                   break
        else:
            return single

# Time Complexity : O(n^2)
# Space Complexity : O(1)