# Method-2
def decompressEncodedList(lst):
    length = len(lst)
    result = []
    for i in range(0, length , 2):
        result.append([lst[i + 1]] * lst[i])
        
    return [item for sublist in result for item in sublist]
    
# Time Complexity : O(n)