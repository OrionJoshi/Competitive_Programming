# Method-1 Iterative method

def smallerNumbers(lst):
    length = len(lst)
    result = []

    for i in range(length):
        count = 0
        for j in range(length):
            if i == j:
                continue
            else:
                if lst[i] > lst[j]:
                    count += 1
        result.append(count)
    return result
    
# Time Complexity : O(n^2)
# Space Complexity : O(n)