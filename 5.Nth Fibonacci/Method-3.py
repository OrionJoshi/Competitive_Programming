# Method-3: recusive with memonization method

def getNthFib(n, memoize = { 1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n -2, memoize)
        return memoize[n]


# Time Complexity:  O(n)
# Space Complexity: O(n)
