# Method-1

def numEquivDominoPairs(dominoes):
    d = {}

    for i in dominoes:
        i = tuple(i)
        if i[::-1] in d:
            d[i[::-1]] += 1
        elif i in d:
            d[i] += 1
        else:
            d[i] = 0

    return sum([(i * (i + 1))//2 for i in d.values()])

# Time Complexity : O(n)
# Space Complexity : O(n)