# Method-1

def minDistance( word1, word2):
    h, w = len(word1) + 1, len(word2) + 1
    pre = [i for i in range(w)]

    for i in range(1, h):
        cur = [i for _ in range(w)]
        for j in range(1, w):
            cur[j] = min(pre[j-1] + (word1[i-1] != word2[j-1]), pre[j] + 1, cur[j-1] + 1)
        pre = cur

    return pre[-1]

# Time Complexity : O(n*m)
# Space Complexity : O(n)