# Method-1 Using Hash table

def destCity(paths):
    lenght = len(paths)
    mapping = {}
    
    for i in range(lenght):
        mapping[paths[i][0]] = paths[i][1]
    
    currentCity = paths[0][0]
    while True:
        if currentCity not in mapping:
            break
        currentCity = mapping[currentCity]
        
    return currentCity

# Time Complexity : O(n)
# Space Complexity : O(n)