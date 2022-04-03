# Method-1

def countVowelStrings(n):
    a = [1] * 5
    
    for _ in range(1, n):
        for i in range(1, 5):
            a[i] += a[i-1]

    return sum(a)

# Time Complexity : O(n)
# Space Complexity : O(1)