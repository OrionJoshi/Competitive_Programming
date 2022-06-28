# Method-1

def largestMerge(word1, word2):
    ans = []
    ptr1 = ptr2 = 0

    while ptr1 < len(word1) and ptr2 < len(word2): 
        if word1[ptr1:] > word2[ptr2:]: 
            ans.append(word1[ptr1])
            ptr1 += 1
        else: 
            ans.append(word2[ptr2])
            ptr2 += 1

    return "".join(ans) + word1[ptr1:] + word2[ptr2:]

# Time Complexity : O(n)
# Space Complexity : O(n)