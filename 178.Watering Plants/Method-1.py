# Method-1

def wateringPlants(plants, capacity):
    ans = 0
    can = capacity
    for i, x in enumerate(plants): 
        if can < x: 
            ans += 2*i
            can = capacity
        ans += 1
        can -= x
    return ans

# Time Complexity : O(n)
# Space Complexity : O(1)