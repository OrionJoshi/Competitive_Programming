# Method-1 Iterative

def anagramMapping(list1, list2):
    lenght = len(list1)
    output = []
    
    for i in range(lenght):
        output.append(list2.index(list1[i]))
        
    return output

# Time Complexity : O(n^2)
# Space Complexity : O(n)