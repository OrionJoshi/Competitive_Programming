# Method-2 Using List Comprehension

def anagramMapping(list1, list2):
    
    return [list2.index(list1[i]) for i in range(len(list1))]

# Time Complexity : O(n^2)
# Space Complexity : O(1)