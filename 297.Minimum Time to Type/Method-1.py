#Method-1

def minTimeToType(word):
    count = 0
    ini = 'a'
    for i in word:
        x = abs(ord(i) - ord(ini))
        count += min(x, 26-x) + 1
        ini = i
    return count

# Time Complexity : O(n)
# Space Complexity : O(1)