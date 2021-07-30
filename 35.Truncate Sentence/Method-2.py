# Method-2 

def truncateSentence(sen, k):
    lst = list(sen.split(" "))
    return " ".join(lst[0: k])

# Time Complexity : O(n)
# Space Complexity : O(1)