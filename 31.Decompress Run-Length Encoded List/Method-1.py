# Method-1
def decompressEncodedList(lst):
    length = len(lst)
    result = []
    
    for i in range(0, length, 2):
        current = lst[i]
        while current > 0:
            result.append(lst[i + 1])
            current -= 1
    return result
        
# # Time Complexity : O(n*m) where n is length of list
#                             m is maximum frequency numbers