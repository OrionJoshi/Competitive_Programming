# Method-2 Using List Comprehension

def buildArray(lst):
    return [lst[lst[i]] for i in range(len(lst))]

# Time Complexity : O(n)
# Space Complexity : O(n)